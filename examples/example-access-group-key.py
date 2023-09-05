# An example how to create a CA key for a access group and delete it.
# Import the PrivX python library.
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

# eplace with the params of the access group ID and ca key ID
ACCESS_GROUP_ID = "ACCESS_GROUP_ID"
CA_ID = "CA_ID"

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


def get_access_group_CA_key(access_group_id):
    result = api.get_access_group_CA_key(access_group_id)
    if result.ok:
        return result.data
    else:
        print(result.data.get("details"))
        sys.exit()


def delete_access_group_CA_key(access_group_id, ca_id):
    result = api.delete_access_group_CA_key(access_group_id, ca_id)
    if result.ok:
        print(result)
        return
    else:
        print(result.data.get("details"))
        sys.exit()


def main():
    ca_id = get_access_group_CA_key(ACCESS_GROUP_ID)
    print(ca_id)
    delete_access_group_CA_key(ACCESS_GROUP_ID, ca_id)


if __name__ == "__main__":
    main()
