# An example how to use PrivX API for host import using json.
# Requires Python 3.6+
import json

# Import the PrivX python library.
import privx_api
import config

# Read the host source file.
with open("example-host-import.json", 'r') as f:
    hosts = json.loads(f.read())

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")

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
            if resp.ok():
                for role in resp.data().get("items"):
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
    if resp.ok():
        print("Host created.")
    else:
        print("Host creation failed.")
        print(resp.data())
