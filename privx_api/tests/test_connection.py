from unittest import mock

import pytest

from privx_api.exceptions import InternalAPIException
from privx_api.privx_api import PrivXAPI


@pytest.mark.parametrize(
    "connection_info",
    [
        (
            {
                "hostname": "",
                "hostport": 2322,
                "ca_cert": None,
                "oauth_client_id": "",
                "oauth_client_secret": "",
            }
        ),
    ],
)
def test_connection_with_exception(connection_info):
    api = PrivXAPI(**connection_info)
    with mock.patch("http.client.HTTPSConnection.putrequest"):
        with pytest.raises(InternalAPIException):
            api.authenticate("", "")
