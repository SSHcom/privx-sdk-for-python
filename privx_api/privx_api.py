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
from privx_api.auth import AuthAPI
from privx_api.connection_manager import ConnectionManagerAPI
from privx_api.host_store import HostStoreAPI
from privx_api.license_manager import LicenseManagerAPI
from privx_api.monitor_service import MonitorServiceAPI
from privx_api.role_store import RoleStoreAPI
from privx_api.settings_service import SettingsServiceAPI
from privx_api.trail_index import TrailIndexAPI
from privx_api.user_store import UserStoreAPI
from privx_api.vault import VaultAPI
from privx_api.workflow_engine import WorkFlowEngineAPI


class PrivXAPI(
    AuthAPI,
    ConnectionManagerAPI,
    HostStoreAPI,
    LicenseManagerAPI,
    MonitorServiceAPI,
    RoleStoreAPI,
    SettingsServiceAPI,
    TrailIndexAPI,
    UserStoreAPI,
    VaultAPI,
    WorkFlowEngineAPI,
):
    """
    Instance for PrivX API library.
    """
