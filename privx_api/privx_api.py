#
# Copyright (c) 2019 SSH Communications Security Corp.
#
# See the LICENSE file for the details on licensing.
#


# Requires Python 3.6+

# https://docs.python.org/3/library/urllib.html
# https://docs.python.org/3/library/ssl.html
# https://docs.python.org/3/library/http.html
# https://docs.python.org/3/library/base64.html
# https://docs.python.org/3/library/json.html

#
# PrivX API lib response.
#
from privx_api.api_proxy import ApiProxyAPI
from privx_api.auth import AuthAPI
from privx_api.authorizer import AuthorizerAPI
from privx_api.connection_manager import ConnectionManagerAPI
from privx_api.db_proxy import DbProxyAPI
from privx_api.host_store import HostStoreAPI
from privx_api.license_manager import LicenseManagerAPI
from privx_api.monitor_service import MonitorServiceAPI
from privx_api.network_access_manager import NetworkAccessManagerAPI
from privx_api.role_store import RoleStoreAPI
from privx_api.secrets_manager import SecretsManagerAPI
from privx_api.settings_service import SettingsServiceAPI
from privx_api.trail_index import TrailIndexAPI
from privx_api.user_store import UserStoreAPI
from privx_api.vault import VaultAPI
from privx_api.workflow_engine import WorkFlowEngineAPI


class PrivXAPI(
    ApiProxyAPI,
    AuthAPI,
    AuthorizerAPI,
    ConnectionManagerAPI,
    DbProxyAPI,
    HostStoreAPI,
    LicenseManagerAPI,
    MonitorServiceAPI,
    NetworkAccessManagerAPI,
    RoleStoreAPI,
    SecretsManagerAPI,
    SettingsServiceAPI,
    TrailIndexAPI,
    UserStoreAPI,
    VaultAPI,
    WorkFlowEngineAPI,
):
    """
    Instance for PrivX API library.
    """
