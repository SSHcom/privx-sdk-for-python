# Import the PrivX python library.
import json
import privx_api
import config

# Replace with the name of the secret you want to fetch
SECRET_NAME = "Name of the secret"

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


def get_secret(name: str) -> str:
    """
    Return the data of the secret with the given name

    Parameters:
        name (str): Name of the target secret
    Returns:
        The secret data JSON.
    """
    secret = api.get_secret(name)
    if secret.ok():
        return secret.data()["data"]
    else:
        return secret.data()["details"]


def main():
    secret = get_secret(SECRET_NAME)
    print(json.dumps(secret, indent=4))


if __name__ == '__main__':
    main()
