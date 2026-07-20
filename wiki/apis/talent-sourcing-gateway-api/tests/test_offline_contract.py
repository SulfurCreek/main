"""TSG-E1/E2/E5：offline contract 驗證（不需憑證，直接對 spec 內 examples 與定義自檢）。"""

RECOMMEND = "/v1/recommend"

EXPECTED_ERROR_CODES = {
    "INVALID_JSON",
    "INVALID_QUERY",
    "MULTIPLE_URLS",
    "UNSUPPORTED_URL",
    "INVALID_API_KEY",
    "JOB_NOT_FOUND",
    "JD_SOURCE_ERROR",
    "RECOMMENDATION_ERROR",
    "JD_SOURCE_TIMEOUT",
    "RECOMMENDATION_TIMEOUT",
}
EXPECTED_ERROR_RESPONSES = {"400", "403", "404", "502", "504"}
LEAK_MARKERS = ("http://", "https://", "Traceback", "x-api-key", "secret", "Secret")


def test_tsg_e1_success_examples_conform_to_schema(spec, validate):
    examples = spec["paths"][RECOMMEND]["post"]["responses"]["200"]["content"][
        "application/json"
    ]["examples"]
    assert set(examples) == {"success", "noResult"}
    for name, ex in examples.items():
        body = ex["value"]
        validate(body, "RecommendResponse")
        assert body["metadata"]["result_count"] == len(body["recommendations"]), name


def test_tsg_e2_error_examples_conform_and_do_not_leak(spec, validate):
    responses = spec["components"]["responses"]
    assert set(responses) == {"BadRequest", "Forbidden", "NotFound", "BadGateway", "GatewayTimeout"}
    for name, resp in responses.items():
        body = resp["content"]["application/json"]["example"]
        validate(body, "ErrorResponse")
        message = body["error"]["message"]
        assert message, name
        for marker in LEAK_MARKERS:
            assert marker not in message, f"{name}: message 疑似洩漏（{marker}）"


def test_tsg_e5_spec_completeness(spec):
    codes = set(spec["components"]["schemas"]["ErrorDetail"]["properties"]["code"]["enum"])
    assert codes == EXPECTED_ERROR_CODES

    schemas = spec["components"]["schemas"]
    assert schemas["RecommendMetadata"]["properties"]["input_mode"]["enum"] == ["text", "url", "url_text"]
    assert schemas["SourceMetadata"]["properties"]["type"]["enum"] == ["direct", "104", "1111"]
    assert schemas["QuerySuggestion"]["properties"]["status"]["enum"] == [
        "not_needed",
        "generated",
        "unavailable",
    ]

    recommend_responses = spec["paths"][RECOMMEND]["post"]["responses"]
    assert EXPECTED_ERROR_RESPONSES | {"200"} == set(recommend_responses)

    # 所有 schema 都必須關閉 additionalProperties
    for name, schema in schemas.items():
        assert schema.get("additionalProperties") is False, name

    # /health 無 auth；/v1/recommend 要 ApiKeyAuth
    assert spec["paths"]["/health"]["get"]["security"] == []
    assert spec["paths"][RECOMMEND]["post"]["security"] == [{"ApiKeyAuth": []}]
