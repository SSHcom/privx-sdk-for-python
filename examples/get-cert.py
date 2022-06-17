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

# The parameters of the API call
# NOTE: Make sure that you have the "Use with PrivX Agent" permisson in your role
conf = {
    # User's public key (MANDATORY)
    "public_key": "xxxxxx AAAAB3NzaC1yc2EAAAADAQABAAABgQCxtVsIEteDnxF+KeMgjm88KmRr6E36iIkks5J+1b9byWno/dC8vnelz+iUBadjUEsVGfmrzbASxXlRU7pwdJgOn31+2ycHxQttR56wuPvghMDa/UQSip9zPnJgigygTUygPvdDgD3jqmYA3EcQx+FC9r316HqlFOnZqunWS9SP2gY1ws/O4MtSSYE4//54q7J21S6amFouIaQL1+8Sx54QTtssGSxxiza+D7ltbP1hk+iJzFVJqUHTiHJo3XiGRuuVwteck2Gsj/twqRauLhyT1FDSOLLP5oTg4693Adg48aM/HTm+amuzA7offIecaXiS3alMum3d0jnx4sA6NJ/ozJpgv8pyisD3+WOM1fIhwwYnVHl0tb+1SV/HFepiV890zSvrhj//nyD7TApc1aVnPNlMTIRqhe10+AjakRRlH8oakXYGQd3OiDm9ig9mKZ5A9V12hbLlub4n/m0UoqZdCmMhl8SLiHUIgJZBdDrlJux4b9suJMFSmHL1cSttHrE= blalbla",
    # UUID of role that is used for accessing the target host (Optional)
    "roleid": "",
    # Target hots service: SSH, RDP or WEB (Optional)
    "service": "",
    # Target username (Optional)
    "username": "",
    # Target hostname (Optional)
    "hostname": "",
    # Target host UUID (Optional)
    "hostid": "",
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
# Return 2 certificates (SHA2-512 + RSA) in a list
#


def get_cert(target_host_config):
    cert = api.get_target_host_credentials(target_host_config)
    if cert.ok:
        certificates = cert.data.get("certificates")
        if certificates is None or len(certificates) == 0:
            print(cert.data)
            sys.exit(1)

        return [c.get("data_string", "") for c in certificates]
    else:
        print(cert.data.get("details"))
        sys.exit()


def clean_pubkey(pubKey):
    _prefix, key_data, *_suffix = pubKey.split(" ")
    return key_data.replace("=", "")


def main():
    # Cleaning the padding to have a key usable by the API
    conf["public_key"] = clean_pubkey(conf["public_key"])

    # Example
    certList = get_cert(conf)
    for i in range(len(certList)):
        print(f"{'-'*12} Cert{i+1}{'-'*12}\n{certList[i]}")


if __name__ == "__main__":
    main()
