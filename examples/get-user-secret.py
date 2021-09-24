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
SECRET_NAME = "Code2"
# Replace with the owner id of the secret that you want
SECRET_OWNER = "2d92b82a-cde4-4837-74e9-d7209d139903"

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


def get_user_secret(owner: str, name: str) -> str:
    """
    Return the data of the secret with the given name and owner

    Parameters:
        owner (str): Owner id
        name (str): Name of the target secret
    Returns:
        The secret data JSON.
    """
    secret = api.get_user_secret(owner, name)
    if secret.ok:
        return secret.data["data"]
    else:
        return secret.data["details"]


def main():
    secret = get_user_secret(SECRET_OWNER, SECRET_NAME)
    print(json.dumps(secret, indent=4))


if __name__ == "__main__":
    main()
