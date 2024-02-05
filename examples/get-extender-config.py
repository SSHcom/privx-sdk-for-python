# Download a pre-configured deployment script.

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


# The trusted client ID for the extender config (required)
EXTENDER_CONFIG_ID = ""
OUTPUT_FILE = f"extender-{EXTENDER_CONFIG_ID}-config.toml"


def main():
    if not EXTENDER_CONFIG_ID:
        print("Specify the EXTENDER_CONFIG_ID variable before running this script.")
        sys.exit(1)

    response = api.get_extender_config(trusted_client_id=EXTENDER_CONFIG_ID)

    if not response.ok:
        print("Failed to get extender config")
        sys.exit(1)

    with open(OUTPUT_FILE, "w") as f:
        for char in response.iter_content():
            f.write(char.decode("utf-8"))

    print(f"Extender config written to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
