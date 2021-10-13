# An example for fetching PrivX audit events.
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

# Initialize the API.
api = privx_api.PrivXAPI(
    config.HOSTNAME,
    config.HOSTPORT,
    config.CA_CERT,
    config.OAUTH_CLIENT_ID,
    config.OAUTH_CLIENT_SECRET,
)

# Authenticate.
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)


# Optional parameters for filtering results.
# Check the PrivX API documentation for additional supported parameters.
SEARCH_PARAMETERS = {
    "start_time": "2021-08-01T00:00:00Z",
    "end_time": "2021-10-01T00:00:00Z",
    "session_id": "607977d7-4791-4ec4-795f-ab0af1ad8eb4"
}


def main():
    response = api.search_audit_events(audit_event_params=SEARCH_PARAMETERS)

    print(response.data)

    if response.ok:
        print("OK")
    else:
        print("ERROR: Failed to fetch audit events!")


if __name__ == "__main__":
    main()
