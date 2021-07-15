# An example how to use PrivX API for host creation.
# Requires Python 3.6+

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


HOST_DNS = "test.privx.ssh.com"
HOST_IP = "192.168.0.10"


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

# Search role ID for host account mapping.
role_id = ""
resp = api.get_roles()
if resp.ok:
    for role in resp.data.get("items"):
        if role.get("name") == "privx-admin":
            role_id = role.get("id")
if role_id == "":
    print("Failed to get role ID.")

# Create host.
data = {
    "common_name": "api-test",
    "addresses": [HOST_DNS, HOST_IP],
    "services": [
        {
            "service": "SSH",
            "address": HOST_IP,
            "port": 22,
            "source": "UI",
        },
    ],
    "principals": [
        {
            "principal": "root",
            "passphrase": "secret",
            "source": "UI",
            "roles": [
                {
                    "id": role_id,
                },
            ],
        },
    ],
}

resp = api.create_host(data)
if resp.ok:
    print("Host created.")
else:
    print("Host creation failed.")
    print(resp.data)
