"""
This example fetches a trail file and prints stdin events seen in the trail.

"""

import base64
import getopt
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


FORMAT = "jsonl"

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


def get_connection(conn_id: str):
    """Fetch connection object"""
    connection = api.get_connection(conn_id)
    if connection.ok:
        return connection.data

    print(connection.data["details"])
    sys.exit(1)


def get_connections_data():
    offset = 0
    limit = 1000
    resp = api.search_connections(
        connection_params={"type": ["SSH"]}, offset=offset, limit=limit
    )
    if resp.ok:
        data_load = resp.data
        data_items = data_load["items"]
        count = data_load["count"] - limit
        while count > 0:
            offset = offset + limit
            resp = api.search_connections(
                connection_params={"type": ["SSH"]}, offset=offset, limit=limit
            )
            if resp.ok:
                data_load = resp.data
                data_items = data_items + data_load["items"]
                count = count - limit
        audited_data_items = []
        for data in data_items:
            if data.get("audit_enabled"):
                audited_data_items.append(data["id"])
        return audited_data_items
    else:
        error = "Get users Connection data operation failed:"
        process_error(error)


def create_trail_session(conn_id: str, chan_id: str):
    """Create sessionId for trail log download"""
    session = api.create_trail_log_download_handle(conn_id, chan_id)
    if session.ok:
        return session.data

    print(session.data["details"])
    sys.exit(1)


def download_trail_log(conn_id: str, chan_id: str, sess_id: str, log_format: str):
    """Download trail log"""
    trail = api.download_trail_log(conn_id, chan_id, sess_id, log_format)
    if trail.ok:
        return b"".join(trail.iter_content()).decode()

    sys.exit(1)


def print_trail(trail: str, s_string, details):
    """Parse and print trail log"""
    trail_lines = trail.splitlines()
    input_str = ""
    for line_item in trail_lines:
        line = json.loads(line_item)
        if line["type"] == "stdin":
            input_event = base64.b64decode(line["data"]).decode("latin1")
            if input_event == "\r":
                if s_string:
                    if s_string in line["ts"][0:19] + " " + input_str:
                        print(details + line["ts"][0:19] + " " + input_str)
                else:
                    print(details + line["ts"][0:19] + " " + input_str)
                input_str = ""
            else:
                input_str += input_event


def process_connections(connections, SEARCH_STRING):
    for connection in connections:
        if "channels" in connection.get("trail", ""):
            for channel in connection["trail"]["channels"]:
                channel_status = channel["protocol_file"]["status"]
                if channel["type"] == "shell" and channel_status != "UNCLEAN_CLOSE":
                    # Get a session ID for trail download
                    session = create_trail_session(connection["id"], channel["id"])
                    # Get the trail
                    trail_log = download_trail_log(
                        connection["id"], channel["id"], session["session_id"], FORMAT
                    )
                    # Parse the trail
                    details = (
                        "\r\nstdin conn "
                        + connection["id"]
                        + " chan "
                        + channel["id"]
                        + " : "
                    )
                    print_trail(trail_log, SEARCH_STRING, details)


def usage():
    print("")
    print(sys.argv[0], " -h or --help")
    print(sys.argv[0], " -c connection_id")
    print(sys.argv[0], " -c bb175019-89ed-47b2-55a4-3b407648463f")
    print(sys.argv[0], " -c connection_id -s search_string")
    print(sys.argv[0], " -c bb175019-89ed-47b2-55a4-3b407648463f -s uptime")
    print(sys.argv[0], " -s search_string")
    print(sys.argv[0], " -s uptime")
    print(sys.argv[0], " --connection-id connection_id --search-string search_string")


def process_error(messages):
    print(messages)
    sys.exit(2)


def main():
    SEARCH_STRING = False
    CONNECTION_ID = False
    if len(sys.argv) > 5 or len(sys.argv) == 4 or len(sys.argv) == 1:
        usage()
        sys.exit(2)
    try:
        opts, args = getopt.getopt(
            sys.argv[1:], "hc:s:", ["help", "connection-id=", "search-string="]
        )
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-c", "--connection-id"):
            CONNECTION_ID = arg
        elif opt in ("-s", "--search-string"):
            SEARCH_STRING = arg
        else:
            usage()
    """Fetch the connection, create sessionId, download trail and parse it."""
    connections = []
    if CONNECTION_ID:
        connections.append(dict(get_connection(CONNECTION_ID)))
    else:
        connection_ids = get_connections_data()
        for id in connection_ids:
            connections.append(dict(get_connection(id)))
    process_connections(connections, SEARCH_STRING)


if __name__ == "__main__":
    main()
