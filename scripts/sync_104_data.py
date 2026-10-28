#!/usr/bin/env python3
import os
import sys
import json
import re
import copy
from datetime import datetime, timezone
from urllib.parse import urlparse

def _clean_env(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("\"", "'"):
        value = value[1:-1].strip()
    return value


R2_ENDPOINT_URL = _clean_env("R2_ENDPOINT_URL")
R2_ACCESS_KEY_ID = _clean_env("R2_ACCESS_KEY_ID")
R2_SECRET_ACCESS_KEY = _clean_env("R2_SECRET_ACCESS_KEY")
R2_BUCKET_NAME = _clean_env("R2_BUCKET_NAME")

if R2_ENDPOINT_URL:
    parsed = urlparse(R2_ENDPOINT_URL if "://" in R2_ENDPOINT_URL else "https://" + R2_ENDPOINT_URL)
    R2_ENDPOINT_URL = f"{parsed.scheme}://{parsed.netloc}" if parsed.scheme == "https" and parsed.netloc and parsed.hostname and not parsed.username and not parsed.password else ""

TARGET_DIR = "career/targets/104"
JOBS_FILE = os.path.join(TARGET_DIR, "jobs.json")
COMPANIES_FILE = os.path.join(TARGET_DIR, "companies.json")
STATE_FILE = os.path.join(TARGET_DIR, "sync-state.json")

MAX_OBJECT_BYTES = 5 * 1024 * 1024  # 5 MB
MAX_ITEMS_PER_BATCH = 500
URL_PATTERN = re.compile(r"^https://([a-zA-Z0-9_-]+\.)?104\.com\.tw/[a-zA-Z0-9_/?=&.%-]+$")
ID_PATTERN = re.compile(r"^[a-zA-Z0-9_-]{1,64}$")

ALLOWED_TOP_KEYS = {"schema_version", "batch_id", "fetched_at", "source", "jobs", "companies"}
ALLOWED_JOB_KEYS = {"job_id", "company_id", "title", "url", "description", "location"}
ALLOWED_COMPANY_KEYS = {"company_id", "name", "url"}


class SyncFatalError(Exception):
    """重大不可復原錯誤，必須使工作流終止失敗 (Exit 1)"""
    pass


class TimestampCorruptedError(Exception):
    """既有資料時間戳損毀，必須使工作流終止 (Exit 2)"""
    pass


def parse_iso_utc(ts_str: str) -> datetime:
    """精確解析 ISO-8601 時間字串，保留微秒並統一至 UTC 時區"""
    if not isinstance(ts_str, str) or not ts_str:
        raise ValueError("時間格式必須為非空字串")
    normalized = ts_str.replace("Z", "+00:00")
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def to_iso_z(dt: datetime) -> str:
    """轉換為標準 UTC ISO-8601 字串 (保留完整微秒精度)"""
    utc_dt = dt.astimezone(timezone.utc)
    if utc_dt.microsecond > 0:
        return utc_dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return utc_dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def _no_duplicate_keys(pairs):
    """防止 JSON Key 重複衝突"""
    d = {}
    for k, v in pairs:
        if k in d:
            raise ValueError(f"JSON 物件中發現重複的 Key: '{k}'")
        d[k] = v
    return d


def validate_and_sanitize_batch(payload, expected_batch_id: str = None) -> tuple[bool, str, dict]:
    """嚴格檢驗與清洗批次 Schema (防重複 ID、防型別繞過、防路徑不符)"""
    if not isinstance(payload, dict):
        return False, "Payload 必須為 JSON Object", {}

    unknown_top = set(payload.keys()) - ALLOWED_TOP_KEYS
    if unknown_top:
        return False, f"Payload 含有未授權欄位: {sorted(unknown_top)}", {}

    if payload.get("schema_version") != 1:
        return False, "不支援的 schema_version (必須為數值 1)", {}

    if payload.get("source") != "104":
        return False, "source 必須為 '104'", {}

    batch_id = payload.get("batch_id")
    if not isinstance(batch_id, str) or not ID_PATTERN.match(batch_id):
        return False, f"非法 batch_id 格式: {batch_id}", {}

    if expected_batch_id and batch_id != expected_batch_id:
        return False, f"批次內容 batch_id ({batch_id}) 與檔案路徑名稱 ({expected_batch_id}) 不符", {}

    try:
        fetched_dt = parse_iso_utc(payload.get("fetched_at"))
        fetched_iso = to_iso_z(fetched_dt)
    except Exception as e:
        return False, f"非法 fetched_at 時間格式: {e}", {}

    raw_jobs = payload.get("jobs", [])
    raw_companies = payload.get("companies", [])
    if not isinstance(raw_jobs, list) or not isinstance(raw_companies, list):
        return False, "jobs 與 companies 必須為 Array", {}

    if len(raw_jobs) > MAX_ITEMS_PER_BATCH or len(raw_companies) > MAX_ITEMS_PER_BATCH:
        return False, f"單批筆數超過上限 ({MAX_ITEMS_PER_BATCH})", {}

    seen_job_ids = set()
    clean_jobs = []
    for j in raw_jobs:
        if not isinstance(j, dict):
            return False, "job 項目必須為 Object", {}
        unknown_j = set(j.keys()) - ALLOWED_JOB_KEYS
        if unknown_j:
            return False, f"job 含有未授權欄位: {sorted(unknown_j)}", {}

        jid = j.get("job_id")
        cid = j.get("company_id", "")
        title = j.get("title")
        url = j.get("url")
        desc = j.get("description", "")
        loc = j.get("location", "")

        if not isinstance(jid, str) or not ID_PATTERN.match(jid):
            return False, f"非法 job_id: {jid}", {}
        if jid in seen_job_ids:
            return False, f"同一批次內發現重複的 job_id: {jid}", {}
        seen_job_ids.add(jid)

        if cid and (not isinstance(cid, str) or not ID_PATTERN.match(cid)):
            return False, f"非法 company_id: {cid}", {}
        if not isinstance(title, str) or not (1 <= len(title) <= 300):
            return False, "title 缺失或長度超限 (1-300 字元)", {}
        if not isinstance(url, str) or len(url) > 500 or not URL_PATTERN.match(url):
            return False, f"非法職缺網址: {url}", {}
        if not isinstance(desc, str) or len(desc) > 20000:
            return False, "description 格式錯誤或超過 20000 字元", {}
        if not isinstance(loc, str) or len(loc) > 200:
            return False, "location 格式錯誤或超過 200 字元", {}

        clean_jobs.append({
            "job_id": jid,
            "company_id": cid,
            "title": title,
            "url": url,
            "description": desc,
            "location": loc,
            "fetched_at": fetched_iso,
        })

    seen_comp_ids = set()
    clean_companies = []
    for c in raw_companies:
        if not isinstance(c, dict):
            return False, "company 項目必須為 Object", {}
        unknown_c = set(c.keys()) - ALLOWED_COMPANY_KEYS
        if unknown_c:
            return False, f"company 含有未授權欄位: {sorted(unknown_c)}", {}

        cid = c.get("company_id")
        name = c.get("name")
        url = c.get("url", "")

        if not isinstance(cid, str) or not ID_PATTERN.match(cid):
            return False, f"非法 company_id: {cid}", {}
        if cid in seen_comp_ids:
            return False, f"同一批次內發現重複的 company_id: {cid}", {}
        seen_comp_ids.add(cid)

        if not isinstance(name, str) or not (1 <= len(name) <= 300):
            return False, "公司名稱缺失或長度超限 (1-300 字元)", {}
        if url and (not isinstance(url, str) or len(url) > 500 or not URL_PATTERN.match(url)):
            return False, f"非法公司網址: {url}", {}

        clean_companies.append({
            "company_id": cid,
            "name": name,
            "url": url,
            "fetched_at": fetched_iso,
        })

    return True, "OK", {
        "batch_id": batch_id,
        "fetched_dt": fetched_dt,
        "fetched_iso": fetched_iso,
        "jobs": clean_jobs,
        "companies": clean_companies,
    }


def apply_batch_transactional(payload: dict, jobs_db: dict, companies_db: dict, state_db: dict, expected_batch_id: str = None) -> tuple[bool, str]:
    """
    以交易式 (All-or-Nothing) 將批次套用至資料庫：
    - 回傳 (True, "APPLIED"): 資料或狀態有實質更新。
    - 回傳 (False, "SKIPPED"): 已處理過或無新資料，未產生任何修改。
    - 回傳 (False, "REJECTED"): 批次無效被隔離捨棄，未修改資料，不標記為已處理。
    - 遇到損毀時間戳拋出 TimestampCorruptedError，不標記已處理，使整體程序中斷。
    """
    processed = set(state_db.get("processed_batches", []))
    batch_id = payload.get("batch_id") if isinstance(payload, dict) else None
    if batch_id and batch_id in processed:
        return False, "SKIPPED_ALREADY_PROCESSED"

    ok, msg, clean = validate_and_sanitize_batch(payload, expected_batch_id=expected_batch_id)
    if not ok:
        print(f"[REJECT] 批次校驗失敗 ({batch_id}): {msg}")
        return False, f"REJECTED_{msg}"

    batch_dt = clean["fetched_dt"]
    pending_jobs = {}
    pending_comps = {}

    # 1. 預審查 jobs 項目
    for j in clean["jobs"]:
        jid = j["job_id"]
        existing = jobs_db["jobs"].get(jid)
        if existing:
            try:
                existing_dt = parse_iso_utc(existing.get("fetched_at", ""))
            except Exception as e:
                # 規範 4：既有時間戳無法解析，Fail-Closed 中止，絕不覆蓋，保留重試
                raise TimestampCorruptedError(f"既有職缺 [{jid}] 之 fetched_at 損毀 ({e})。中止批次套用！")

            if existing_dt >= batch_dt:
                continue  # 既有資料較新，安全略過

        if existing != j:
            pending_jobs[jid] = j

    # 2. 預審查 companies 項目
    for c in clean["companies"]:
        cid = c["company_id"]
        existing = companies_db["companies"].get(cid)
        if existing:
            try:
                existing_dt = parse_iso_utc(existing.get("fetched_at", ""))
            except Exception as e:
                raise TimestampCorruptedError(f"既有公司 [{cid}] 之 fetched_at 損毀 ({e})。中止批次套用！")

            if existing_dt >= batch_dt:
                continue

        if existing != c:
            pending_comps[cid] = c

    # 3. 確定全體驗證無誤，執行原子性寫入
    changed = False
    if pending_jobs:
        jobs_db["jobs"].update(pending_jobs)
        changed = True
    if pending_comps:
        companies_db["companies"].update(pending_comps)
        changed = True

    # 標記此批次處理成功
    state_db.setdefault("processed_batches", []).append(clean["batch_id"])
    state_db["processed_batches"] = sorted(set(state_db["processed_batches"]))

    return (True if changed else False), ("APPLIED" if changed else "NOOP_RECORDED")


def load_target_databases_fail_closed():
    """
    規範 2：讀取本地資料庫時嚴格 Fail-Closed。
    明確區分『檔案不存在』與『檔案存在但損毀/缺少欄位』。
    """
    os.makedirs(TARGET_DIR, exist_ok=True)

    def _read_file(filepath, default_key):
        if not os.path.exists(filepath):
            return {default_key: {} if default_key != "processed_batches" else []}
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f, object_pairs_hook=_no_duplicate_keys)
        except Exception as e:
            raise SyncFatalError(f"嚴重錯誤：資料檔 {filepath} 損毀或非合法 JSON ({e})。終止執行，防止資料覆蓋！")

        if default_key not in data:
            raise SyncFatalError(f"嚴重錯誤：資料檔 {filepath} 缺少必要頂層鍵值 '{default_key}'！")
        return data

    jobs_db = _read_file(JOBS_FILE, "jobs")
    companies_db = _read_file(COMPANIES_FILE, "companies")
    state_db = _read_file(STATE_FILE, "processed_batches")
    state_db.setdefault("last_sync_at", None)

    return jobs_db, companies_db, state_db


def save_json(filepath, data):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")


# ==============================================================================
# 自我驗證測試套件 (Self-Tests)
# ==============================================================================
def run_self_tests():
    """執行全套 8 項自我驗證測試，證明上述安全防護均可正確觸發"""
    print("=== 開始執行同步邏輯自我驗證測試 ===")

    # 基準乾淨環境
    jobs_db = {"jobs": {}}
    companies_db = {"companies": {}}
    state_db = {"processed_batches": [], "last_sync_at": None}

    base_batch = {
        "schema_version": 1,
        "batch_id": "20261027T120000Z-base01",
        "fetched_at": "2026-10-27T12:00:00.000Z",
        "source": "104",
        "jobs": [{
            "job_id": "job1",
            "company_id": "comp1",
            "title": "資深產品經理",
            "url": "https://www.104.com.tw/job/job1",
            "description": "職缺說明 v1",
            "location": "台北市"
        }],
        "companies": [{
            "company_id": "comp1",
            "name": "測試科技公司",
            "url": "https://www.104.com.tw/company/comp1"
        }]
    }

    # 初次套用
    applied, msg = apply_batch_transactional(base_batch, jobs_db, companies_db, state_db, expected_batch_id="20261027T120000Z-base01")
    assert applied is True and msg == "APPLIED"

    # 測試 1：重複批次傳入 -> 命中略過，不修改資料庫，不重複追加狀態
    snap_jobs = copy.deepcopy(jobs_db)
    snap_state = copy.deepcopy(state_db)
    applied, msg = apply_batch_transactional(base_batch, jobs_db, companies_db, state_db, expected_batch_id="20261027T120000Z-base01")
    assert applied is False and msg == "SKIPPED_ALREADY_PROCESSED"
    assert jobs_db == snap_jobs and state_db == snap_state
    print("[PASS] 測試 1：重複批次成功跳過且狀態不變。")

    # 測試 2：傳入較舊資料 -> 不覆蓋新資料 (精度至微秒)
    older_batch = copy.deepcopy(base_batch)
    older_batch["batch_id"] = "20261026T120000Z-old001"
    older_batch["fetched_at"] = "2026-10-26T12:00:00.000Z"
    older_batch["jobs"][0]["title"] = "舊標題 (不應覆蓋)"
    applied, msg = apply_batch_transactional(older_batch, jobs_db, companies_db, state_db, expected_batch_id="20261026T120000Z-old001")
    assert applied is False and msg == "NOOP_RECORDED"
    assert jobs_db["jobs"]["job1"]["title"] == "資深產品經理"
    assert "20261026T120000Z-old001" in state_db["processed_batches"]
    print("[PASS] 測試 2：較舊資料成功被忽略，未覆蓋現存較新記錄。")

    # 測試 3：傳入非法欄位或惡意檔案路徑 -> 嚴格拒絕，不更新資料，不標記為已處理
    malicious_batch = {
        "schema_version": 1,
        "batch_id": "20261028T120000Z-hack01",
        "fetched_at": "2026-10-28T12:00:00.000Z",
        "source": "104",
        "target_file": "../../etc/shadow",  # 惡意未授權欄位
        "jobs": [],
        "companies": []
    }
    applied, msg = apply_batch_transactional(malicious_batch, jobs_db, companies_db, state_db, expected_batch_id="20261028T120000Z-hack01")
    assert applied is False and "REJECTED" in msg
    assert "20261028T120000Z-hack01" not in state_db["processed_batches"]
    print("[PASS] 測試 3：非法欄位被嚴格攔截拒絕，未記錄至已處理狀態。")

    # 測試 4：空清單 (爬蟲抓取失敗) -> 不清空現存資料
    empty_batch = {
        "schema_version": 1,
        "batch_id": "20261028T130000Z-empty1",
        "fetched_at": "2026-10-28T13:00:00.000Z",
        "source": "104",
        "jobs": [],
        "companies": []
    }
    applied, msg = apply_batch_transactional(empty_batch, jobs_db, companies_db, state_db, expected_batch_id="20261028T130000Z-empty1")
    assert applied is False and msg == "NOOP_RECORDED"
    assert "job1" in jobs_db["jobs"] and "comp1" in companies_db["companies"]
    print("[PASS] 測試 4：空清單未清空現有資料庫。")

    # 測試 5：檔名與 batch_id 不符 (全新未處理批次) -> 實際命中路徑驗證並拒絕
    mismatched_batch = {
        "schema_version": 1,
        "batch_id": "20261028T140000Z-realid",
        "fetched_at": "2026-10-28T14:00:00.000Z",
        "source": "104",
        "jobs": [],
        "companies": []
    }
    applied, msg = apply_batch_transactional(mismatched_batch, jobs_db, companies_db, state_db, expected_batch_id="different-file-name")
    assert applied is False and "與檔案路徑名稱" in msg
    assert "20261028T140000Z-realid" not in state_db["processed_batches"]
    print("[PASS] 測試 5：檔名與 batch_id 不符被準確拒絕，未毒化狀態。")

    # 測試 6：既有資料時間戳損毀時 Fail-Closed 中止，且修復後可重新執行
    corrupt_db = {"jobs": {"job1": {"title": "原有職缺", "fetched_at": "CORRUPTED_TS"}}}
    retry_batch = {
        "schema_version": 1,
        "batch_id": "20261028T150000Z-retryable",
        "fetched_at": "2026-10-28T15:00:00.000Z",
        "source": "104",
        "jobs": [{
            "job_id": "job1",
            "title": "新職缺標題",
            "url": "https://www.104.com.tw/job/job1",
            "description": "新內文",
            "location": "台北市"
        }],
        "companies": []
    }
    try:
        apply_batch_transactional(retry_batch, corrupt_db, companies_db, state_db, expected_batch_id="20261028T150000Z-retryable")
        assert False, "應拋出 TimestampCorruptedError"
    except TimestampCorruptedError:
        pass
    assert "20261028T150000Z-retryable" not in state_db["processed_batches"]

    # 人工修復時間戳後重新套用 -> 應順利成功
    corrupt_db["jobs"]["job1"]["fetched_at"] = "2026-10-25T00:00:00.000Z"
    applied, msg = apply_batch_transactional(retry_batch, corrupt_db, companies_db, state_db, expected_batch_id="20261028T150000Z-retryable")
    assert applied is True
    assert corrupt_db["jobs"]["job1"]["title"] == "新職缺標題"
    assert "20261028T150000Z-retryable" in state_db["processed_batches"]
    print("[PASS] 測試 6：時間戳損毀時安全阻擋且未登記已處理，修復後成功重新套用。")

    # 測試 7：單一批次內含重複 ID -> 拒絕整批
    dup_id_batch = {
        "schema_version": 1,
        "batch_id": "20261028T160000Z-dupid",
        "fetched_at": "2026-10-28T16:00:00.000Z",
        "source": "104",
        "jobs": [
            {"job_id": "dup1", "title": "A", "url": "https://www.104.com.tw/job/a"},
            {"job_id": "dup1", "title": "B", "url": "https://www.104.com.tw/job/b"}
        ],
        "companies": []
    }
    applied, msg = apply_batch_transactional(dup_id_batch, jobs_db, companies_db, state_db, expected_batch_id="20261028T160000Z-dupid")
    assert applied is False and "重複的 job_id" in msg
    print("[PASS] 測試 7：批次內重複 ID 成功被攔截。")

    # 測試 8：JSON 含有重複 Key -> 拒絕
    dup_key_json = '{"schema_version": 1, "source": "104", "source": "fake"}'
    try:
        json.loads(dup_key_json, object_pairs_hook=_no_duplicate_keys)
        assert False, "應攔截重複 Key"
    except ValueError:
        pass
    print("[PASS] 測試 8：重複 JSON Key 防禦生效。")

    print("=== 全套 8 項自我測試全部通過！ ===")


def main():
    if "--self-test" in sys.argv:
        run_self_tests()
        sys.exit(0)

    if not all([R2_ENDPOINT_URL, R2_ACCESS_KEY_ID, R2_SECRET_ACCESS_KEY, R2_BUCKET_NAME]):
        print("錯誤：缺少必要的 R2 連線環境變數設定", file=sys.stderr)
        sys.exit(1)

    try:
        jobs_db, companies_db, state_db = load_target_databases_fail_closed()
    except SyncFatalError as e:
        print(f"[FATAL] {e}", file=sys.stderr)
        sys.exit(1)

    before_jobs = copy.deepcopy(jobs_db)
    before_comps = copy.deepcopy(companies_db)
    before_batches = set(state_db.get("processed_batches", []))

    try:
        import boto3
        from botocore.config import Config

        s3 = boto3.client(
            service_name="s3",
            endpoint_url=R2_ENDPOINT_URL,
            aws_access_key_id=R2_ACCESS_KEY_ID,
            aws_secret_access_key=R2_SECRET_ACCESS_KEY,
            region_name="auto",
            config=Config(s3={"addressing_style": "virtual"}, retries={"max_attempts": 3, "mode": "standard"})
        )
        paginator = s3.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=R2_BUCKET_NAME, Prefix="incoming/")

        objects = []
        for page in pages:
            for obj in page.get("Contents", []):
                if obj["Key"].endswith(".json"):
                    objects.append((obj["Key"], obj.get("Size", 0)))
    except Exception as e:
        print(f"[FATAL] 連線或讀取 R2 收件匣失敗 ({e})。終止執行！", file=sys.stderr)
        sys.exit(1)

    objects.sort(key=lambda x: x[0])
    print(f"在 R2 收件匣找到 {len(objects)} 個批次物件。")

    processed_set = set(state_db.get("processed_batches", []))

    for key, size in objects:
        if size > MAX_OBJECT_BYTES:
            print(f"[REJECT] 檔案超過 5MB 上限 ({size} bytes): {key}")
            continue

        filename_batch_id = os.path.basename(key)[:-5]
        if filename_batch_id in processed_set:
            continue

        try:
            resp = s3.get_object(Bucket=R2_BUCKET_NAME, Key=key)
            raw_bytes = resp["Body"].read(MAX_OBJECT_BYTES + 1)
            if len(raw_bytes) > MAX_OBJECT_BYTES:
                print(f"[REJECT] 實際內容超過大小上限: {key}")
                continue
            payload = json.loads(raw_bytes.decode("utf-8"), object_pairs_hook=_no_duplicate_keys)
        except Exception as e:
            print(f"[REJECT] 無法讀取或 JSON 格式非法 ({key}): {e}")
            continue

        try:
            apply_batch_transactional(payload, jobs_db, companies_db, state_db, expected_batch_id=filename_batch_id)
        except TimestampCorruptedError as e:
            print(f"[FATAL] {e}", file=sys.stderr)
            sys.exit(2)

        processed_set = set(state_db.get("processed_batches", []))

    has_data_changed = (before_jobs != jobs_db or before_comps != companies_db)
    has_state_changed = (before_batches != set(state_db.get("processed_batches", [])))

    if has_data_changed or has_state_changed:
        state_db["last_sync_at"] = to_iso_z(datetime.now(timezone.utc))
        save_json(JOBS_FILE, jobs_db)
        save_json(COMPANIES_FILE, companies_db)
        save_json(STATE_FILE, state_db)
        print("同步完成，資料庫與狀態已成功寫入！")
    else:
        print("無新批次或無資料異動。")


if __name__ == "__main__":
    main()