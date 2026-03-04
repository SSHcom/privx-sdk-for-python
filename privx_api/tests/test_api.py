from enum import Enum
from http import HTTPStatus
from unittest import mock

import pytest

from privx_api.base import format_path_components
from privx_api.enums import UrlEnum
from privx_api.exceptions import InternalAPIException
from privx_api.privx_api import PrivXAPI
from privx_api.utils import get_value


def test_urls():
    with pytest.raises(InternalAPIException):
        api = PrivXAPI("", "", "", "", "")
        api._get_url("not real")

    assert api._get_url(UrlEnum.AUTH.AUTHORIZE) != ""


@pytest.mark.parametrize(
    "base_url, args, expected",
    [
        ("/api/{id}/search", {"id": "a/b"}, "/api/a%2Fb/search"),
        ("/api/search?", {}, "/api/search?"),
    ],
)
def test_format_path_components(base_url, args, expected):
    assert format_path_components(base_url, **args) == expected


@pytest.mark.parametrize(
    "base_url, args",
    [
        ("/api/{id}/search", {"id": []}),
        ("/api/search/{ids}", {"ids": [1, 2, 3]}),
        ("/api/search/{ids}", {"ids": {"one": 1}}),
        ("/api/search/{ids}", {"ids": None}),
        ("/api/search/{ids}", {"ids": (1, 2, 3)}),
    ],
)
def test_format_path_components_negative(base_url, args):
    with pytest.raises(InternalAPIException):
        format_path_components(base_url, **args)


@pytest.mark.parametrize(
    "urlname, path_params, query_params, expected",
    [
        (
            UrlEnum.ROLE_STORE.MEMBERS,
            {"role_id": "123"},
            {"limit": 500},
            "/role-store/api/v1/roles/123/members?limit=500",
        ),
    ],
)
def test_build_url(urlname, path_params, query_params, expected):
    api = PrivXAPI("", "", "", "", "")
    assert api._build_url(urlname, path_params, query_params) == expected


@pytest.mark.parametrize(
    "url_name, expected_url",
    [
        ("AUTH.AUTHORIZE", "/auth/api/v1/oauth/authorize"),
        ("HOST_STORE.HOST", "/host-store/api/v1/hosts/{host_id}"),
        ("HOST_STORE.SEARCH", "/host-store/api/v1/hosts/search"),
        ("CONNECTION_MANAGER.SEARCH", "/connection-manager/api/v1/connections/search"),
    ],
)
def test_url_enum_get(url_name, expected_url):
    assert UrlEnum.get(url_name) == expected_url


@pytest.mark.parametrize(
    "url_name, expected_url",
    [
        ("TEST", "/asdasd/asd/test"),
        ("FAKE", None),
        ("", None),
        (None, None),
        (123, None),
    ],
)
def test_url_enum_get_exception_similar_url_name(url_name, expected_url):
    class TestEnumFirst:
        TEST = "TEST"
        urls = {TEST: "/asdasd/asd/test"}

    class TestEnumSecond:
        TEST = "TEST"
        urls = {TEST: "/asdasd/asd/test"}

    class FakeEnum(UrlEnum):
        CASE_1 = TestEnumFirst
        CASE_2 = TestEnumSecond

    with pytest.raises(InternalAPIException):
        FakeEnum.get(url_name)


@pytest.mark.parametrize(
    "value, expected_value",
    [
        ({"key": 123123}, '{"key": 123123}'),
        (
            "9293a478-0db1-4090-638d-22684820e230",
            "9293a478-0db1-4090-638d-22684820e230",
        ),
        ("{'key': 'value'}", "{'key': 'value'}"),
    ],
)
def test_make_body_params(value, expected_value):
    api = PrivXAPI("", "", "", "", "")
    assert api._make_body_params(value) == expected_value


class DummyEnum(Enum):
    SAMPLE = "VaLue"


def test_get_search_params_coercion():
    api = PrivXAPI("", 0, "", "", "")

    params = api._get_search_params(
        truthy=True,
        falsy=False,
        enum_value=DummyEnum.SAMPLE,
        mixed_case="FoObAr",
        keep_int=5,
        skip_none=None,
    )

    assert params == {
        "truthy": "true",
        "falsy": "false",
        "enum_value": "VaLue",
        "mixed_case": "foobar",
        "keep_int": 5,
    }


def test_get_search_params_normalizes_common_query_params_for_server_compat():
    api = PrivXAPI("", 0, "", "", "")

    params = api._get_search_params(
        filter="AcCeSsIbLe",
        sortdir="ASC",
        query="SomeText",
        verbose=True,
    )

    assert params == {
        "filter": "accessible",
        "sortdir": "asc",
        "query": "sometext",
        "verbose": "true",
    }


class DummyHTTPResponse:
    def __init__(self, payload: bytes, *, status: HTTPStatus = HTTPStatus.OK) -> None:
        self._payload = payload
        self.status = status

    def read(self, chunk_size: int = -1) -> bytes:
        if chunk_size == -1:
            data = self._payload
            self._payload = b""
            return data
        chunk = self._payload[:chunk_size]
        self._payload = self._payload[chunk_size:]
        return chunk

    def close(self) -> None:
        return None


def test_api_response_helper_passes_last_response_headers():
    api = PrivXAPI("", 0, "", "", "")
    api._store_response_headers({"Content-Type": "application/json"})

    resp = api._api_response(HTTPStatus.OK, HTTPStatus.OK, b'{"k": "v"}')

    assert resp.headers["content-type"] == "application/json"
    assert resp.status == HTTPStatus.OK
    assert resp.ok is True


def test_stream_response_helper_passes_last_response_headers():
    api = PrivXAPI("", 0, "", "", "")
    api._store_response_headers({"X-Request-Id": "req-123"})

    resp = api._stream_api_response(DummyHTTPResponse(b"abc"), HTTPStatus.OK)

    assert resp.headers["x-request-id"] == "req-123"
    assert resp.status == HTTPStatus.OK
    assert resp.ok is True


def test_api_response_helper_marks_non_expected_status_as_not_ok():
    api = PrivXAPI("", 0, "", "", "")
    api._store_response_headers({"Content-Type": "application/json"})

    resp = api._api_response(HTTPStatus.BAD_REQUEST, HTTPStatus.OK, b'{"error":"x"}')

    assert resp.ok is False
    assert resp.data == {"status": HTTPStatus.BAD_REQUEST, "details": {"error": "x"}}


def test_stream_response_helper_marks_non_expected_status_as_not_ok():
    api = PrivXAPI("", 0, "", "", "")
    api._store_response_headers({"X-Request-Id": "req-123"})

    resp = api._stream_api_response(
        DummyHTTPResponse(b"abc", status=HTTPStatus.BAD_REQUEST),
        HTTPStatus.OK,
    )

    assert resp.ok is False
    assert resp.status == HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize(
    "params, exp_result",
    [
        (
            {
                "method": "GET",
                "url_name": UrlEnum.CONNECTION_MANAGER.CONNECTIONS,
                "query_params": {"offset": "111", "limit": "20"},
            },
            {
                "method": "GET",
                "url": "/connection-manager/api/v1/connections?offset=111&limit=20",
                "headers": {
                    "Content-type": "application/json",
                    "Authorization": "Bearer ",
                },
            },
        ),
        (
            {
                "method": "GET",
                "url_name": UrlEnum.CONNECTION_MANAGER.TRAIL_LOG_SESSION_ID,
                "query_params": {"format_param": "111", "filter_param": "20"},
                "path_params": {
                    "connection_id": "1",
                    "channel_id": "1",
                    "session_id": "1",
                },
            },
            {
                "method": "GET",
                "url": "/connection-manager/api/v1/connections/1/"
                "channel/1/log/1?format_param=111&filter_param=20",
                "headers": {
                    "Content-type": "application/json",
                    "Authorization": "Bearer ",
                },
            },
        ),
        (
            {
                "method": "GET",
                "url_name": UrlEnum.CONNECTION_MANAGER.TERMINATE_CONNECTION_ID,
                "query_params": {"format_param": "111", "filter_param": "20"},
                "path_params": {
                    "connection_id": "1",
                },
                "body": {"body_params": "just params"},
            },
            {
                "method": "GET",
                "url": "/connection-manager/api/v1/terminate"
                "/connection/1?format_param=111&filter_param=20",
                "headers": {
                    "Content-type": "application/json",
                    "Authorization": "Bearer ",
                },
                "body": '{"body_params": "just params"}',
            },
        ),
        (
            {
                "method": "POST",
                "url_name": UrlEnum.CONNECTION_MANAGER.TERMINATE_CONNECTION_ID,
                "path_params": {
                    "connection_id": "1",
                },
                "body": "body as a str",
            },
            {
                "method": "POST",
                "url": "/connection-manager/api/v1/terminate/connection/1",
                "headers": {
                    "Content-type": "application/json",
                    "Authorization": "Bearer ",
                },
                "body": "body as a str",
            },
        ),
    ],
)
def test_build_request(params, exp_result):
    api = PrivXAPI("", "", "", "", "")
    with mock.patch.object(PrivXAPI, "_authenticate"):
        assert sorted(api._build_request(**params)) == sorted(exp_result)


@pytest.mark.parametrize(
    "val, default_val, exp_val",
    [
        ("", "", ""),
        ("data", "", "data"),
        (0, 123, 0),
        ([], [1, 2, 3], []),
        (None, dict(), {}),
        (None, [], []),
        (None, None, None),
    ],
)
def test_get_value(val, default_val, exp_val):
    assert get_value(val, default_val) == exp_val
