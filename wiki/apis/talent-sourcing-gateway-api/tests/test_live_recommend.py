"""TSG-A/B/C/D/E3/E4：live 案例，實際打 dev API。

缺憑證時整批 skip（pending credentials）；每案驗 status code、content-type、回應 schema
（Schemathesis conformance 三件套思路）。報告與 log 一律不得輸出 x-api-key 值。
"""
import json

import pytest
import requests

from conftest import require_env_url

TIMEOUT = 60
CLIENT_ID = "api-test-vm"


def post_recommend(live, query, client_id=CLIENT_ID, raw_body=None, extra=None, headers=None):
    url = live["base_url"] + "/v1/recommend"
    h = dict(headers if headers is not None else live["headers"])
    if raw_body is not None:
        h["Content-Type"] = "application/json"
        return requests.post(url, data=raw_body, headers=h, timeout=TIMEOUT)
    body = {"query": query, "client_id": client_id}
    if extra:
        body.update(extra)
    return requests.post(url, json=body, headers=h, timeout=TIMEOUT)


def assert_ok(resp, validate):
    assert resp.status_code == 200, resp.text[:500]
    assert resp.headers.get("Content-Type", "").startswith("application/json")
    body = resp.json()
    validate(body, "RecommendResponse")
    return body


def assert_error(resp, validate, status, codes):
    assert resp.status_code == status, resp.text[:500]
    body = resp.json()
    validate(body, "ErrorResponse")
    assert body["error"]["code"] in codes, body["error"]
    return body


# ---------- A 正常案例 ----------

def test_tsg_a1_text_query(live, validate):
    body = assert_ok(post_recommend(live, "熟悉 Python、AWS 與 REST API 的後端工程師"), validate)
    md = body["metadata"]
    assert md["input_mode"] == "text"
    assert md["source"]["type"] == "direct"
    assert md["source"]["url"] is None and md["source"]["job_id"] is None


def test_tsg_a2_url_104(live, validate):
    url = require_env_url("TSG_TEST_URL_104")
    body = assert_ok(post_recommend(live, url), validate)
    md = body["metadata"]
    assert md["input_mode"] == "url"
    assert md["source"]["type"] == "104"
    assert md["source"]["job_id"]


def test_tsg_a3_url_1111(live, validate):
    url = require_env_url("TSG_TEST_URL_1111")
    body = assert_ok(post_recommend(live, url), validate)
    md = body["metadata"]
    assert md["input_mode"] == "url"
    assert md["source"]["type"] == "1111"


def test_tsg_a4_url_with_text(live, validate):
    url = require_env_url("TSG_TEST_URL_104")
    body = assert_ok(post_recommend(live, f"{url} 希望候選人具備帶領團隊經驗"), validate)
    md = body["metadata"]
    assert md["input_mode"] == "url_text"
    assert "帶領團隊" in md["query_used"]


def test_tsg_a5_zero_result_returns_suggestion(live, validate):
    body = assert_ok(
        post_recommend(live, "精通 COBOL 與量子退火演算法的水下考古潛水員（限外太空經驗）"),
        validate,
    )
    md = body["metadata"]
    if md["result_count"] == 0:
        assert body["recommendations"] == []
        assert md["suggestion"]["status"] in {"generated", "unavailable"}
    else:
        pytest.xfail("此查詢意外有結果，零結果情境未觸發（記錄於報告）")


def test_tsg_a6_health_no_auth(live, validate):
    resp = requests.get(live["base_url"] + "/health", timeout=10)
    assert resp.status_code == 200, resp.text[:500]
    body = resp.json()
    validate(body, "HealthResponse")
    assert body == {"status": "ok"}


# ---------- B 邊界值 ----------

def test_tsg_b1_query_min_length_1(live, validate):
    assert_ok(post_recommend(live, "P"), validate)


def test_tsg_b2_query_max_length_20000(live, validate):
    prefix = "Python 後端工程師 "
    query = prefix + "A" * (20000 - len(prefix))
    assert len(query) == 20000
    body = assert_ok(post_recommend(live, query), validate)
    assert body["metadata"]["query_truncated"] in (True, False)


def test_tsg_b3_query_empty(live, validate):
    resp = post_recommend(live, "")
    assert_error(resp, validate, 400, {"INVALID_QUERY", "INVALID_JSON"})


def test_tsg_b4_query_over_max(live, validate):
    resp = post_recommend(live, "A" * 20001)
    assert_error(resp, validate, 400, {"INVALID_QUERY", "INVALID_JSON"})


def test_tsg_b5_client_id_length_bounds(live, validate):
    assert_ok(post_recommend(live, "Python 工程師", client_id="a"), validate)
    assert_ok(post_recommend(live, "Python 工程師", client_id="a" * 64), validate)


def test_tsg_b6_client_id_over_max(live, validate):
    resp = post_recommend(live, "Python 工程師", client_id="a" * 65)
    assert_error(resp, validate, 400, {"INVALID_QUERY", "INVALID_JSON"})


def test_tsg_b7_client_id_bad_pattern(live, validate):
    resp = post_recommend(live, "Python 工程師", client_id="crm 服務@!")
    assert_error(resp, validate, 400, {"INVALID_QUERY", "INVALID_JSON"})


# ---------- C Auth ----------

def test_tsg_c1_missing_api_key(live, validate):
    resp = post_recommend(live, "Python 工程師", headers={})
    assert_error(resp, validate, 403, {"INVALID_API_KEY"})


def test_tsg_c2_invalid_api_key(live, validate):
    resp = post_recommend(live, "Python 工程師", headers={"x-api-key": "invalid-key-for-test"})
    assert_error(resp, validate, 403, {"INVALID_API_KEY"})


def test_tsg_c3_health_without_key(live, validate):
    test_tsg_a6_health_no_auth(live, validate)


# ---------- D 錯誤碼 ----------

def test_tsg_d1_invalid_json(live, validate):
    resp = post_recommend(live, None, raw_body='{"query": ')
    assert_error(resp, validate, 400, {"INVALID_JSON"})


def test_tsg_d2_missing_and_extra_fields(live, validate):
    url = live["base_url"] + "/v1/recommend"
    for body in (
        {"client_id": CLIENT_ID},                                   # 缺 query
        {"query": "Python 工程師"},                                  # 缺 client_id
        {"query": "Python 工程師", "client_id": CLIENT_ID, "x": 1},  # 多餘欄位
    ):
        resp = requests.post(url, json=body, headers=live["headers"], timeout=TIMEOUT)
        assert_error(resp, validate, 400, {"INVALID_QUERY", "INVALID_JSON"})


def test_tsg_d3_multiple_urls(live, validate):
    resp = post_recommend(
        live, "https://www.104.com.tw/job/8siqc https://www.1111.com.tw/job/123456"
    )
    assert_error(resp, validate, 400, {"MULTIPLE_URLS"})


def test_tsg_d4_unsupported_url(live, validate):
    resp = post_recommend(live, "https://www.linkedin.com/jobs/view/123456")
    assert_error(resp, validate, 400, {"UNSUPPORTED_URL"})


def test_tsg_d5_job_not_found(live, validate):
    url = require_env_url("TSG_TEST_URL_DEAD")
    resp = post_recommend(live, url)
    assert_error(resp, validate, 404, {"JOB_NOT_FOUND"})


@pytest.mark.skip(reason="TSG-D6 需 mock 下游：JD 來源異常（502 JD_SOURCE_ERROR）")
def test_tsg_d6_jd_source_error():
    pass


@pytest.mark.skip(reason="TSG-D7 需 mock 下游：推薦服務異常（502 RECOMMENDATION_ERROR）")
def test_tsg_d7_recommendation_error():
    pass


@pytest.mark.skip(reason="TSG-D8 需 mock 下游：JD 來源逾時（504 JD_SOURCE_TIMEOUT）")
def test_tsg_d8_jd_source_timeout():
    pass


@pytest.mark.skip(reason="TSG-D9 需 mock 下游：推薦服務逾時（504 RECOMMENDATION_TIMEOUT）")
def test_tsg_d9_recommendation_timeout():
    pass


# ---------- E Contract（live）----------

def test_tsg_e3_rank_ascending_and_count(live, validate):
    body = assert_ok(post_recommend(live, "熟悉 Python、AWS 與 REST API 的後端工程師"), validate)
    ranks = [r["rank"] for r in body["recommendations"]]
    assert ranks == sorted(ranks)
    assert body["metadata"]["result_count"] == len(body["recommendations"])


def test_tsg_e4_suggestion_state_consistency(live, validate):
    body = assert_ok(post_recommend(live, "熟悉 Python、AWS 與 REST API 的後端工程師"), validate)
    sug = body["metadata"]["suggestion"]
    if sug["status"] == "not_needed":
        assert sug["suggested_query"] is None and sug["reason"] is None
    elif sug["status"] == "generated":
        assert sug["suggested_query"]
