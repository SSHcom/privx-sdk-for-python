# Requires Python 3.6+
import sys
import csv
import getopt

# Import the PrivX python library.
import privx_api

# Import the configs.
import config

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


def get_roles():
    resp = api.get_roles()
    if resp.ok():
        data_load = resp.data()
        roles_data = {}
        for role_data in data_load['items']:
            name = role_data['name']
            roles_data[name] = role_data['id']
        return roles_data
    else:
        error = "Get Roles operation failed:"
        process_error(error)


def get_users(role_id):
    resp = api.get_role_members(role_id)
    if resp.ok():
        data_load = resp.data()
        users_data = {}
        for user_data in data_load['items']:
            user = user_data['principal']
            users_data[user] = user_data['id']
        return users_data
    else:
        error = "Get users operation failed:"
        process_error(error)


def get_connection_data(uid, user):
    resp = api.search_connections(user_id=[uid])
    if resp.ok():
        data_load = resp.data()
        connections_data = {}
        all_data = []
        connections_data["user"] = user
        for connection_data in data_load['items']:
            data = ("type,target_host_address,"
                    "target_host_account,connected,disconnected")
            data_list = data.split(',')
            for p in data_list:
                if p in ("connected", "disconnected"):
                    connection_data[p] = connection_data[p].split(".")[0]
                connections_data[p] = connection_data[p]
            all_data.append(dict(connections_data))
        return all_data
    else:
        error = "Get users Connection data operation failed:"
        process_error(error)


def export_connection_data(user, users_data, header_printed=False):
    output_csvfile = user+"_connection_data.csv"
    users = {}
    if user == "ALL":
        users = users_data
    else:
        users[user] = users_data[user]
    with open(output_csvfile, "w") as f:
        print("Writing Connection data to", output_csvfile, end=' ')
        for user, uid in users.items():
            connection_data = get_connection_data(uid, user)
            for data in connection_data:
                w = csv.DictWriter(f, data.keys())
                if not header_printed:
                    w.writeheader()
                    header_printed = True
                w.writerow(data)
    print("\nDone")


def usage():
    print("")
    print(sys.argv[0], " -h or --help")
    print(sys.argv[0], " -u user1")
    print(sys.argv[0], " --user ALL")


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    user = "ALL"
    if (len(sys.argv) > 3):
        usage()
        sys.exit(2)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:", ["help", "user="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-u", "--user"):
            user = arg
        else:
            usage()
    roles_data = get_roles()
    role_id = roles_data['privx-user']
    users_data = get_users(role_id)
    if (user == "ALL" or user in users_data.keys()):
        export_connection_data(user, users_data)
    else:
        print(user+" user not found")
        sys.exit(2)


if __name__ == '__main__':
    main()
