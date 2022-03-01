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


PUB_KEY_PATH = "path to the public key"
CERT_PREFIX = "ssh-rsa-cert-v01@openssh.com"

conf = {
    "public_key": "public key",
    "role_id": "a role UUID with which to request "
    "the certificate (client must be a member)",
    "hostid": "target host UUID",
    "hostname": "target host hostname",
    "username": "target username",
    "service": "SSH",
}


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

#
# Read the pubkey, strip padding and prefix & suffix
#


def read_pubkey(file):
    with open(file, "r") as f:
        _prefix, key_data, *_suffix = f.read().split(" ")
        return key_data.replace("=", "")


def get_cert(target_host_config):
    cert = api.get_target_host_credentials(target_host_config)
    if cert.ok:
        certificates = cert.data.get("certificates")
        if certificates is None or len(certificates) == 0:
            print("Certificates not found")
            sys.exit(1)

        return certificates[0]["data_string"]
    else:
        print(cert.data.get("details"))
        sys.exit()


def main():
    if PUB_KEY_PATH == "" or PUB_KEY_PATH is None:
        print("public key is not declared")
        sys.exit(1)

    conf["public_key"] = read_pubkey(PUB_KEY_PATH)
    cert = get_cert(conf)

    print(cert)


if __name__ == "__main__":
    main()
