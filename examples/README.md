# PrivX SDK Examples

The following examples demonstrates a typical usage scenario. The usage of examples requires Python 3.6+ 

Usage Python Virtual Environment simplify development 

```bash
python3 -m pip install virtualenv
python3 -m venv .env
source .env/bin/activate
pip install git+git://github.com/SSHcom/privx-sdk-for-python.git
```

## Register API Client

You have to register your API client with PrivX before usage. Open PrivX Web UI and go to

```
Settings > Deployment > Integrate With PrivX Using API Clients
```

Click `ADD API CLIENT`, give a human readable API client unique name and suitable permissions. The role permissions for the client varies on the use case, check the PrivX documentation for permission explanation.
Add one or more role by selecting role from list of roles. Adding roles to the API client gives it permissions from that role. For security reasons, only grant permissions that are actually needed.

After the API client creation, you can find the secrets for the client
under credentials section. The config.py must include the OAuth client 
secret ("OAUTH_CLIENT_SECRET"), API Client ID (API_CLIENT_ID) and 
API Client Secret (API_CLIENT_SECRET).

Fill in the missing fields in config.py
* HOSTNAME, the PrivX instance address, like "my.privx.intance.net"
* CA_CERT, the CA certificate, found on the API clients page ("TLS Trust Anchor")
* OAUTH_CLIENT_SECRET, found on the API clients page ("OAuth Client Secret")
* API_CLIENT_ID, found on the API clients page("API Client ID")
* API_CLIENT_SECRET, found on the API clients page("API Client SECRET")


## Example execution of reporting scripts

Get role mapping data (Access Report)
```
$ python3 get-roles-mapping-report.py
Writing role mapping data to access_report.csv
Done
$ head -n2 access_report.csv
user_id,role_name,target_hosts,target_accounts
"jsingh,nhirbli,nsleiman,tnandy,pre-sales",partners-linux-admin,"ec2-18-120-215-133.eu-west-2.compute.amazonaws.com,ip-172-31-10-79.eu-west-2.compute.internal",centos
```

Get connection data for all connections (ALL users or individual user)
```
$ python3 get-access-report.py -h

get-access-report.py  -h or --help
get-access-report.py  -u user1
get-access-report.py  --user ALL

$ python3 get-access-report.py
Writing Connection data to ALL_connection_data.csv
Done
$ head -n3 ALL_connection_data.csv
user,type,mode,authentication_method,target_host_address,target_host_account,connected,disconnected
superuser,SSH,UI,PASSPHRASE,195.20.116.105:22,manager,2019-09-17T13:19:16,2019-09-17T13:19:21
jessica.white,RDP,UI,CERT,ec2-52-203-108-57.compute-1.amazonaws.com,jessica.white,2019-02-07T07:11:43,2019-02-07T07:12:31


$ python3 get-access-report.py -u jimmy.admin
Writing Connection data to jimmy.admin_connection_data.csv
Done
$ head -n3 jimmy.admin_connection_data.csv
user,type,mode,authentication_method,target_host_address,target_host_account,connected,disconnected
jimmy.admin,SSH,UI,CERT,35.158.99.23:22,ec2-user,2019-10-08T20:28:52,2019-10-08T22:01:43
jimmy.admin,WEB,UI,PASSPHRASE,webgw/https://sshdev.signin.aws.amazon.com/console,test.user,2020-03-03T18:54:32,2020-03-03T18:56:23
```

Get hosts data
```
$ python3 get-hosts-report.py
Writing hosts data to hosts_data.csv
Done
$ head -n3 hosts_data.csv
common_name,addresses,users,protocol,audit_enabled,created,updated,updated_by
Ora2PG-VISA,ip-172-31-43-205.eu-west-2.compute.internal,centos,SSH,False,2020-09-16T14:50:13,2021-03-29T12:53:05,
Ora2PG-DOCS,ip-172-31-42-16.eu-west-2.compute.internal,centos,SSH,False,2020-09-29T10:03:47,2021-03-29T12:53:05,
```

Get role members for individual or all roles  
```
$ python3 get-role-members.py -h

get-role-members.py  -h or --help
get-role-members.py  -r role_name
get-role-members.py  --role-name ALL

$python3 get-role-members.py
Writing role members data to ALL_role_members.csv
Done
$ head -n4 ALL_role_members.csv
role_name,principal,full_name,email,samaccountname,windows_account,unix_account,source_type
Network-admin,sakethr,Saketh R,saketh.r@example.com,,sakethr,sakethr,LOCAL
Network-admin,upmdeveloper,upmdeveloper,upmdeveloper@foo.com,,,,LOCAL
privx-admin,juho,Juho R,juhor@example.com,,,,LOCAL

$ python3 get-role-members.py -r UnixAdmins
Writing role members data to UnixAdmins_role_members.csv
Done
$ head -n3 UnixAdmins_role_members.csv
role_name,principal,full_name,email,samaccountname,windows_account,unix_account,source_type
UnixAdmins,jimmy.admin,Jimmy Admin,jimmy.admin@privxdemo.ssh.com,,,,LOCAL
UnixAdmins,rkumar,Rakesh K,rakesh.k@example.com,rkumar,rkumar,rkumar,AD
```

Get/Search connection trails for string
```
$ python3 search-connections-trails.py -h

search-connections-trails.py  -h or --help
search-connections-trails.py  -c connection_id
search-connections-trails.py  -c bb175019-89ed-47b2-55a4-3b407648463f
search-connections-trails.py  -c connection_id -s search_string
search-connections-trails.py  -c bb175019-89ed-47b2-55a4-3b407648463f -s uptime
search-connections-trails.py  -s search_string
search-connections-trails.py  -s uptime
search-connections-trails.py  --connection-id connection_id --search-string search_string

Get connection trail for one connection using connection id
$ python3 search-connections-trails.py -c bb175019-89ed-47b2-55a4-3b407648463f

stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:19 uptime
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:21 sudo su -
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:23 date
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:26 dmidecode
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:28 last
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:35 demicdecode
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:36
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:39 dmidecode
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:52 uname -a
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:53 exit
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:55 exit

Search specific connection for string specified
$ python3 search-connections-trails.py -c bb175019-89ed-47b2-55a4-3b407648463f -s dmi

stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:26 dmidecode
stdin conn bb175019-89ed-47b2-55a4-3b407648463f chan 0 : 2021-07-26T12:51:39 dmidecode


Search for string acorss all connection trails
$ python3 search-connections-trails.py -s eboot

stdin conn 3fce2f47-d6b9-42a4-749a-7cfde7afb0c7 chan 0 : 2020-09-08T10:43:33 reboot
stdin conn 9f6aadac-f3a0-4f08-51bb-d2a2cfcbc10c chan 0 : 2021-02-19T12:06:29 reboot
```
