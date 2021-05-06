"""
This example fetches a trail file and prints stdin events seen in the trail.

"""
import sys
import base64
import json
# Import the PrivX python library.
import privx_api
import config

# Replace with the ID of the connection to output
CONNECTION_ID = "CONNECTION_ID"
FORMAT = "jsonl"

# Initialize the API.
api = privx_api.PrivXAPI(config.HOSTNAME, config.HOSTPORT, config.CA_CERT,
                         config.OAUTH_CLIENT_ID, config.OAUTH_CLIENT_SECRET)

# Authenticate.
# NOTE: fill in your credentials from secure storage, this is just an example
api.authenticate("API client ID", "API client secret")


def get_connection(conn_id: str):
    """Fetch connection object"""
    connection = api.get_connection(conn_id)
    if connection.ok():
        return connection.data()

    print(connection.data()["details"])
    sys.exit(1)


def create_trail_session(conn_id: str, chan_id: str):
    """Create sessionId for trail log download"""
    session = api.create_trail_log_session_id(conn_id, chan_id)
    if session.ok():
        return session.data()

    print(session.data()["details"])
    sys.exit(1)


def download_trail_log(conn_id: str,
                       chan_id: str,
                       sess_id: str,
                       log_format: str):
    """Download trail log"""
    trail = api.download_trail_log(conn_id, chan_id, sess_id, log_format)
    if trail.ok():
        return trail.data()

    print(trail.data()["details"])
    sys.exit(1)


def print_trail(trail: str):
    """Parse and print trail log"""
    trail_lines = trail.splitlines()
    input_str = ""
    for line_item in trail_lines:
        line = json.loads(line_item)
        if line["type"] == "stdin":
            input_event = base64.b64decode(line["data"]).decode("latin1")
            if input_event == "\r":
                print(line["ts"][0:19]+" "+input_str)
                input_str = ""
            else:
                input_str += input_event


def main():
    """Fetch the connection, create sessionId, download trail and parse it."""
    connection = get_connection(CONNECTION_ID)

    # Iterate channels
    for channel in connection["trail"]["channels"]:
        if channel["type"] == "shell":
            # Get a session ID for trail download
            session = create_trail_session(CONNECTION_ID, channel["id"])
            # Get the trail
            trail_log = download_trail_log(CONNECTION_ID,
                                           channel["id"],
                                           session["session_id"],
                                           FORMAT)
            # Parse the trail
            print("\r\nstdin conn "+CONNECTION_ID+" chan "+channel["id"])
            print("------------------------------------------------------")
            print_trail(trail_log)


if __name__ == '__main__':
    main()
