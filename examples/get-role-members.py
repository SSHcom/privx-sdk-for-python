# Requires Python 3.6+
import csv
import getopt
import sys

# Import the configs.
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
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate(config.API_CLIENT_ID, config.API_CLIENT_SECRET)


def get_roles(role_name):
    all_roles_data = []
    resp = api.get_roles()
    if resp.ok:
        data_load = resp.data
        role_id = False
        for role_data in data_load["items"]:
            roles_data = {}
            if role_name != "ALL":
                if role_data["name"] == role_name:
                    roles_data["name"] = role_data["name"]
                    roles_data["id"] = role_data["id"]
                    role_id = True
            else:
                roles_data["name"] = role_data["name"]
                roles_data["id"] = role_data["id"]
                role_id = True
            if roles_data:
                all_roles_data.append(dict(roles_data))
        if role_id:
            return all_roles_data
        else:
            print(role_name + ": Role not found")
            sys.exit(2)
    else:
        error = "Get Roles operation failed:"
        process_error(error)


def get_role_members(roles_data, role_name):
    offset = 0
    limit = 50
    all_data = []
    data = (
        "principal,full_name,email,samaccountname,"
        "windows_account,unix_account,source_type"
    )
    data_list = data.split(",")
    for role_data in roles_data:
        resp = api.get_role_members(
            role_id=role_data["id"],
            offset=offset,
            limit=limit,
        )
        if resp.ok:
            data_load = resp.data
            data_items = data_load["items"]
            count = data_load["count"] - limit
            while count > 0:
                offset = offset + limit
                resp = api.get_role_members(
                    role_id=role_data["id"],
                    offset=offset,
                    limit=limit,
                )
                if resp.ok:
                    data_load = resp.data
                    data_items = data_items + data_load["items"]
                    count = count - limit
            for member in data_items:
                member_data = {}
                member_data["role_name"] = role_data["name"]
                for p in data_list:
                    member_data[p] = member.get(p, "")
                all_data.append(dict(member_data))
        else:
            error = "Get Roles Members operation failed:"
            process_error(error)
    if all_data:
        return all_data
    else:
        print(role_name + ": No Users associated with role")
        sys.exit(2)


def export_role_members_data(roles_data, role_name):
    all_data = []
    output_csvfile = role_name + "_role_members.csv"
    all_data = get_role_members(roles_data, role_name)
    all_data_keys = all_data[0].keys()
    print("Writing role members data to", output_csvfile, end=" ")
    with open(output_csvfile, "w") as f:
        w = csv.DictWriter(f, all_data_keys)
        w.writeheader()
        for data in all_data:
            w.writerow(data)
    print("\nDone")


def usage():
    print("")
    print(sys.argv[0], " -h or --help")
    print(sys.argv[0], " -r role_name")
    print(sys.argv[0], " --role-name ALL")


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    role_name = "ALL"
    if len(sys.argv) > 3:
        usage()
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:", ["help", "role_name="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-r", "--role-name"):
            role_name = arg
        else:
            usage()
    roles_data = get_roles(role_name)
    export_role_members_data(roles_data, role_name)


if __name__ == "__main__":
    main()
