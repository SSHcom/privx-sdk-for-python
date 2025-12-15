import pytest

from privx_api.cookie_jar import RoutingCookieJar


def test_store_and_get_header_respects_domain_and_path():
    jar = RoutingCookieJar()
    jar.store(
        [
            "AWSALB=node-a; Path=/auth; Domain=.example.com",
            "ROUTE=node-b; Path=/api/v2",
        ],
        host="privx.example.com",
        request_path="/auth/login",
    )

    assert (
        jar.get_header("privx.example.com", "/auth/session") == "AWSALB=node-a"
    ), "cookie with matching domain/path should be returned"
    assert (
        jar.get_header("unrelated.com", "/auth/session") is None
    ), "non-matching domain should not receive cookies"
    assert (
        jar.get_header("privx.example.com", "/api/v2/hosts") == "ROUTE=node-b"
    ), "second cookie should be scoped to its own path"


def test_store_without_path_uses_default_path():
    jar = RoutingCookieJar()
    jar.store(
        ["stick=node-1"],
        host="api.example.com",
        request_path="/api/v1/tokens?foo=bar",
    )

    assert jar.get_header("api.example.com", "/api/v1/projects") == "stick=node-1"
    assert jar.get_header("api.example.com", "/status") is None


def test_get_header_drops_expired_cookies(monkeypatch):
    jar = RoutingCookieJar()
    now = {"value": 100}

    def fake_time():
        return now["value"]

    monkeypatch.setattr("privx_api.cookie_jar.time.time", fake_time)

    jar.store(["ROUTE=abc; Max-Age=1"], host="api.example.com", request_path="/")
    now["value"] = 200

    assert jar.get_header("api.example.com", "/") is None
    assert jar._cookies == {}


@pytest.mark.parametrize(
    "request_path, expected",
    [
        ("/api/v1/resource", "/api/v1"),
        ("/api", "/"),
        ("api", "/"),
        ("/", "/"),
        ("", "/"),
    ],
)
def test_default_path(request_path, expected):
    assert RoutingCookieJar._default_path(request_path) == expected


@pytest.mark.parametrize(
    "request_path, cookie_path, expected",
    [
        ("/", "/", True),
        ("/foo/bar", "/foo", True),
        ("/foo", "/foo", True),
        ("/foo", "/foo/bar", False),
        ("/foobar", "/foo", False),
        ("foo/bar", "/foo", True),
    ],
)
def test_path_matches(request_path, cookie_path, expected):
    assert RoutingCookieJar._path_matches(request_path, cookie_path) is expected
