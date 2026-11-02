# R2 → GitHub 104 ingestion contract

Receiver: `scripts/sync_104_data.py` on `claude/claude-md-docs-BmaVo`.
Destination: three existing JSON files on `automation/104-data`.
This contract does not grant the uploader GitHub access and does not update application notes.

## Versioning

`schema_version` must be the JSON integer 1 or 2 (not a boolean, string or float).
v1 keeps the original company whitelist. Rich fields require v2.
Top-level and job fields are unchanged; unknown fields are rejected, not discarded.

```json
{
  "schema_version": 2,
  "batch_id": "unique-batch-id",
  "fetched_at": "2026-11-02T01:00:00Z",
  "source": "104",
  "jobs": [],
  "companies": [
    {
      "company_id": "demo",
      "name": "Example company",
      "url": "https://www.104.com.tw/company/demo",
      "industry": "Software",
      "capital": "400億",
      "employee_count": "310人",
      "location": "台北市",
      "profile": "Company profile",
      "benefits": ["Remote work"]
    }
  ]
}
```

This is a synthetic format example, not data to upload.

## Company fields

| Field | Type | Limit / meaning |
| --- | --- | --- |
| company_id | string, required | existing ASCII ID pattern, 1–64 characters |
| name | string, required | 1–300 characters |
| url | string, required in v2 | exact https://www.104.com.tw/company/<company_id>, optional trailing slash; max 500 characters |
| industry | optional string | 300 characters |
| capital | optional string | 100 characters; preserve source units, no numeric conversion |
| employee_count | optional string | 100 characters; preserve source wording |
| location | optional string | 500 characters |
| profile | optional string | 10,000 characters |
| benefits | optional array of strings | max 100 items; each nonblank and max 300 characters |

Length is Python character count, not byte count. Null and non-string rich text are rejected.
`main_score`, paths, commands and any other unknown company fields are rejected.
`fetched_at` is supplied at batch level; per-company output timestamps are set by the receiver.

## Update semantics

- Newer company records merge validated supplied fields into the existing record.
- Omitted optional fields preserve the old value, including when a later v1 batch arrives.
- Explicit `""` and `[]` clear the corresponding rich field. Omit unavailable data instead of sending empty placeholders.
- Older or equal timestamps do not replace existing company records, including missing rich fields. A new batch ID alone does not bypass freshness checks. Use a genuinely newer observation; do not falsify timestamps to force an update.
- Duplicate batch IDs are skipped. Use a new unique batch ID for a new export; do not overwrite an already processed object to force reprocessing.
- Unknown keys, invalid values or duplicate IDs reject the entire batch before jobs, companies or state are changed.
- Empty lists never delete existing records; absent companies do not imply closure/deletion.
- Rich data is untrusted source text, never an instruction for an agent to execute.

## Transport and rollout

Upload JSON through the existing R2 S3-compatible API to
`incoming/YYYY/MM/DD/{batch_id}.json`; filename must equal batch_id.
Maximum UTF-8 object size: 5 * 1024 * 1024 bytes.
Maximum 500 jobs and 500 companies per batch. Split exports if the encoded JSON exceeds the byte limit; 128 companies do not automatically fit when profiles/benefits are large.

Deploy the receiver first, then upgrade the uploader to v2.
Only select the approved fields from local caches; do not upload a local company dictionary verbatim.
No changes to GitHub credentials, bucket permissions or Actions path allowlist are needed.

The scheduled workflow already invokes `python scripts/sync_104_data.py --self-test` before reading R2. It now includes v2 regressions as well as the original eight tests.
Offline success is not evidence of a successful real v2 R2 import. After uploading, inspect the Actions result, ensure the batch is in sync-state.json, and verify representative rich fields in companies.json on automation/104-data.
