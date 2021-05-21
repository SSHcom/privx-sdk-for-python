# An example how to use PrivX API for host import using json.
# Requires Python 3.6+
import json
import os
import sys

import config

# this importation for demonstration purpose only
# for proper importation of privx_api module
# see https://github.com/SSHcom/privx-sdk-for-python#getting-started
try:
    # Running example with pip-installed SDK
    import privx_api
except ImportError:
    # Running example without installing SDK
    from utils import load_privx_api_lib_path

    load_privx_api_lib_path()
    import privx_api

# Specify the path to the host-data JSON file.
# By default, uses the example-host-import.json from the data directory.
# For more information about host-data syntax, see the
# PrivX-API specifications.
HOST_DATA_FILE = os.path.join(sys.path[0], "data/example-host-import.json")

# Read the host source file.
with open(HOST_DATA_FILE, "r") as f:
    hosts = json.loads(f.read())

# Initialize the API.
api = privx_api.PrivXAPI(
    config.HOSTNAME,
    config.HOSTPORT,
    config.CA_CERT,
    config.OAUTH_CLIENT_ID,
    config.OAUTH_CLIENT_SECRET,
)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)

for hostdata in hosts:
    principals = []
    if len(hostdata.get("accounts")):
        for account in hostdata.get("accounts"):
            item = {
                "principal": account.get("name"),
                "passphrase": account.get("password"),
                "source": "UI",
            }

            # Search role ID for host account mapping.
            roles = {}
            acc_roles = []
            resp = api.get_roles()
            if resp.ok:
                for role in resp.data.get("items"):
                    roles[role.get("name")] = role.get("id")

            for role_name, role_id in roles.items():
                if role_name in account.get("roles"):
                    acc_roles.append({"id": role_id})

            item["roles"] = acc_roles
            principals.append(item)

    # Create host.
    data = {
        "common_name": hostdata.get("name"),
        "addresses": hostdata.get("addresses"),
        "audit_enabled": bool(hostdata.get("audited")),
        "services": hostdata.get("services"),
        "principals": principals,
    }

    resp = api.create_host(data)
    if resp.ok:
        print("Host created.")
    else:
        print("Host creation failed.")
        print(resp.data)
