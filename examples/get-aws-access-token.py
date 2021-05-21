# Requires Python 3.6+
import getopt
import sys

# Import the configs.
import config

# in order to import privx_sdk from current directory
sys.path.append("..")
import privx_api  # noqa E-402

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


def usage():
    print(
        "Example for fetching AWS temporary access token via PrivX role.\n"
        "Requires mapping AWS role to PrivX role in PrivX admin console.\n"
        "If PrivX user has a role with AWS role mapping, you can use '-r awsroleid' "
        "to acquire a token with assumed permissions via PrivX.\n"
    )
    print(sys.argv[0], "-h or --help")
    print(sys.argv[0], "-r awsroleid")
    print(sys.argv[0], "--awsrole awsroleid")
    print(sys.argv[0], "--list")


def print_awsroles(resp):
    if resp.ok:
        print(resp.data)
    else:
        print(resp.data)
        sys.exit(2)


def print_token(resp):
    if resp.ok:
        print(resp.data)
    else:
        print(resp.data)
        sys.exit(2)


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlr:", ["help", "list", "awsrole="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-l", "--list"):
            resp = api.get_aws_role_links()
            print_awsroles(resp)
        elif opt in ("-r", "--awsrole"):
            resp = api.get_aws_token(arg, 900)
            print_token(resp)
        else:
            usage()


if __name__ == "__main__":
    main()
