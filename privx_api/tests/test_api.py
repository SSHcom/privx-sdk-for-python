import pytest

from privx_api.exceptions import InternalAPIException
from privx_api.privx_api import PrivXAPI
from privx_api.base import format_path_components
from privx_api.enums import UrlEnum


def test_urls():
    with pytest.raises(InternalAPIException):
        PrivXAPI._get_url("not real")

    assert PrivXAPI._get_url(UrlEnum.AUTH.AUTHORIZE) != ""


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
    assert PrivXAPI._build_url(urlname, path_params, query_params) == expected


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
