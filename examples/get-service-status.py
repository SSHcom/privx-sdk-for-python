# Example for quickly checking all microservice statuses.
# Print additional information about any microservices
# with non-OK statuses.

import json
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


def main():
    response = api.get_privx_components_status()

    if not response.ok:
        print("ERROR: Failed to fetch component statuses! Exiting..")
        print(response.status)
        sys.exit(1)

    print("Checking for anomalies on PrivX Servers..")

    for server_name, microservices in response.data.items():
        problem_microservices = [m for m in microservices
                                 if m['status']['status_message'] != 'OK']
        if problem_microservices:
            print(f"Potential problems with microservice(s) on {server_name}")
            for problem in problem_microservices:
                print(json.dumps(problem, indent=4))
        else:
            print(f"No problems found on {server_name}")

    print("Checks completed.")


if __name__ == "__main__":
    main()
