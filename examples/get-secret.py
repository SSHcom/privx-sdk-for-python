# Import the PrivX python library.
import json

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

# Replace with the name of the secret you want to fetch
SECRET_NAME = "Name of the secret"

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


def get_secret(name: str) -> str:
    """
    Return the data of the secret with the given name

    Parameters:
        name (str): Name of the target secret
    Returns:
        The secret data JSON.
    """
    secret = api.get_secret(name)
    if secret.ok:
        return secret.data["data"]
    else:
        return secret.data["details"]


def main():
    secret = get_secret(SECRET_NAME)
    print(json.dumps(secret, indent=4))


if __name__ == "__main__":
    main()
