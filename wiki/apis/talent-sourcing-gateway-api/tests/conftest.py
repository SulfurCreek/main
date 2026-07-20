"""Talent Sourcing Gateway API 測試共用 fixtures。

環境變數（見 wiki/api_testing_rules.md §4；缺憑證時 live 案例整批 skip）：
  TSG_API_ID        AWS API Gateway 的 apiId（CloudFormation output）
  TSG_BASE_URL      完整 base URL，設了就優先於 TSG_API_ID
  TSG_API_KEY       x-api-key
  TSG_TEST_URL_104  有效的 104 職缺網址（A2/A4 用）
  TSG_TEST_URL_1111 有效的 1111 職缺網址（A3 用）
  TSG_TEST_URL_DEAD 已下架/不存在的職缺網址（D5 用）
"""
import copy
import os
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft4Validator, RefResolver

SPEC_PATH = Path(__file__).resolve().parent.parent / "spec" / "talent-sourcing-ateway-api_v1.0.1@20260717.yaml"


def _openapi_to_jsonschema(node):
    """OpenAPI 3.0 schema → JSON Schema：把 nullable:true 展開成 type: [t, "null"]。"""
    if isinstance(node, dict):
        node = {k: _openapi_to_jsonschema(v) for k, v in node.items()}
        if node.pop("nullable", False) and "type" in node:
            node["type"] = [node["type"], "null"]
            if "enum" in node and None not in node["enum"]:
                node["enum"] = node["enum"] + [None]
        return node
    if isinstance(node, list):
        return [_openapi_to_jsonschema(v) for v in node]
    return node


@pytest.fixture(scope="session")
def spec():
    with open(SPEC_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def schema_doc(spec):
    """整份 spec 轉成可供 jsonschema 解 $ref 的文件。"""
    return _openapi_to_jsonschema(copy.deepcopy(spec))


@pytest.fixture(scope="session")
def validate(schema_doc):
    """validate(instance, "RecommendResponse") → schema 驗證失敗時 raise。"""

    def _validate(instance, schema_name):
        schema = schema_doc["components"]["schemas"][schema_name]
        resolver = RefResolver(base_uri="", referrer=schema_doc)
        Draft4Validator(schema, resolver=resolver).validate(instance)

    return _validate


@pytest.fixture(scope="session")
def base_url():
    url = os.environ.get("TSG_BASE_URL")
    if url:
        return url.rstrip("/")
    api_id = os.environ.get("TSG_API_ID")
    if api_id:
        return f"https://{api_id}.execute-api.ap-northeast-1.amazonaws.com/dev"
    return None


@pytest.fixture(scope="session")
def api_key():
    return os.environ.get("TSG_API_KEY")


@pytest.fixture
def live(base_url, api_key):
    """live 案例共用前置：缺憑證 → skip（pending credentials）。"""
    if not base_url or not api_key:
        pytest.skip("pending credentials：未設定 TSG_API_ID/TSG_BASE_URL 或 TSG_API_KEY")
    return {"base_url": base_url, "headers": {"x-api-key": api_key}}


def require_env_url(name):
    url = os.environ.get(name)
    if not url:
        pytest.skip(f"需提供測試職缺網址：環境變數 {name} 未設定")
    return url
