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

def get_connection_data(user):
    offset = 0
    limit = 1000
    resp = api.search_connections(offset=offset, limit=limit)
    if resp.ok():
        data_load = resp.data()
        data_items = data_load['items']
        count = data_load['count'] - limit
        while count > 0:
            offset = offset + limit
            resp = api.search_connections(offset=offset, limit=limit)
            data_load = resp.data()
            if resp.ok():
                data_items = data_items + data_load['items']
                count = count - limit
        connections_data = {}
        all_data = []
        data = ("type,mode,authentication_method,target_host_address,"
                "target_host_account,connected,disconnected")
        data_list = data.split(',')
        for connection_data in data_items:
            principal = connection_data['user']['display_name']
            if user in ("ALL", principal):
                connections_data["user"] = connection_data['user']['display_name']
                for p in data_list:
                    if p in ("connected", "disconnected"):
                        connection_data[p] = connection_data[p].split(".")[0]
                    if p == "authentication_method":
                        connection_data[p] = ','.join(connection_data[p])
                    connections_data[p] = connection_data[p]
                all_data.append(dict(connections_data))
        if not len(all_data):
            print("No connection data found for "+user)
            sys.exit(2)
        return all_data
    else:
        error = "Get users Connection data operation failed:"
        process_error(error)


def export_connection_data(user, header_printed=False):
    output_csvfile = user+"_connection_data.csv"
    with open(output_csvfile, "w") as f:
        connection_data = get_connection_data(user)
        print("Writing Connection data to", output_csvfile, end=' ')
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
    export_connection_data(user)

if __name__ == '__main__':
    main()
