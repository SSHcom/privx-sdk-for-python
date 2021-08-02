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
