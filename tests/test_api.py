import pytest

from privx_api import PrivXAPI


def test_urls():
    api = PrivXAPI("bogus", "1234", "", "", "")

    with pytest.raises(Exception):
        api._get_url("not real")

    assert api._get_url("auth.authorize") != ""
