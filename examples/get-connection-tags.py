"""
This example updates connection tags and fetch connection tags.

"""
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

# Replace with the params of the connection tags
CONNECTION_ID = "CONNECTION_ID"
OFFSET = 0
LIMIT = 100
SORTDIR = "asc"
QUERY = ""
CONNECTION_TAGS = ["CONNECTION_TAGS"]

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


def get_connection_tags(offset, limit, sort_dir, query):
    """Fetch connection tags object"""
    connection = api.get_connection_tags(offset, limit, sort_dir, query)
    if connection.ok:
        return connection.data

    print(connection.data["details"])
    sys.exit(1)

def update_connection_tags(conn_id: str, connection_tags):
    """Update connection tags object"""
    result = api.update_connection_tags(conn_id, connection_tags)
    if result.ok:
        return

    print(result.data["details"])
    sys.exit(1)

def main():
    """Update and fetch the connection tags."""
    update_connection_tags(CONNECTION_ID, CONNECTION_TAGS)
    connection_tags = get_connection_tags(OFFSET, LIMIT, SORTDIR, QUERY)
    print(connection_tags)

if __name__ == "__main__":
    main()
