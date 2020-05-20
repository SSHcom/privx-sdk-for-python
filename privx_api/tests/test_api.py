import pytest

from ..privx_api import PrivXAPI, format_path_components


def test_urls():
    with pytest.raises(Exception):
        PrivXAPI._get_url("not real")

    assert PrivXAPI._get_url("auth.authorize") != ""


def test_format_path_components():
    cases = [
        ("/api/{id}/search", {"id": "a/b"}, "/api/a%2Fb/search"),
        ("/api/search?", {}, "/api/search?"),
    ]

    for c in cases:
        frmt_str, args, expected = c
        assert format_path_components(frmt_str, **args) == expected


def test_build_url():
    cases = [
        ("rolestore.roles.members", {"role_id": "123"}, {"limit": 500},
            "/role-store/api/v1/roles/123/members?limit=500"),
    ]

    for c in cases:
        urlname, path_params, query_params, expected = c
        assert PrivXAPI._build_url(
            urlname, path_params, query_params) == expected
