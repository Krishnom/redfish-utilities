import argparse
import redfish

def is_response_ok(status):
    return int(status) < 400

def get_bios_settings(redfish_url, username=None, password=None):
    return fire_redfish_api(redfish_url, username=username, password=password, context='/redfish/v1/System/1')

def get_all(redfish_url, username=None, password=None):
    return fire_redfish_api(redfish_url, username=username, password=password)

def get_cpu_attributes(redfish_url, username=None, password=None):
    pass


def get_boot_attributes(redfish_url, username=None, password=None):
    pass

def get_memory_attributes(redfish_url, username=None, password=None):
    pass
def fire_redfish_api(redfish_url, username='contoso_employee457', password=None, context='/redfish/v1/'):
    print("Creating Client")
    redfish_obj = redfish.redfish_client(base_url=redfish_url, default_prefix='/redfish/v1/', max_retry=3, timeout=10)
    redfish_obj.login(auth="basic", username=username, password=password)
    print("Connected to Redfish")
    print("Getting System Info")
    response = redfish_obj.get(context, None)

    if is_response_ok(response.status):
        return response.text


# if __name__ == '__main__()':
parser = argparse.ArgumentParser(description='Get the BIOS configuration of the host.')
parser.add_argument('--url', dest='host', default='http://localhost:9099',
                    help='URL of the redfish server. for eg. http://127.0.0.1')
parser.add_argument('--username', dest='redfish_username', required=False,
                    help='Username to auth the redfish server')
parser.add_argument('--password', dest='redfish_password', required=False,
                    help='Password to auth the redfish server.')
parser.add_argument('--include', dest='include_configs', default='all',
                    help='Space separated configuration to include. '
                         'Defaults to all. valid values are cpu, memory, bios and all for now. '
                         'e.g. to get only cpu and memory metrics use --include="cpu memory"')
parser.add_argument('--out-file', dest='output_file', required=False, help="Store metrics in the file")

args = parser.parse_args()
print(args)
remote_host = args.host
include_config = [inc.strip() for inc in str(args.include_configs).split()]
redfish_username = args.redfish_username
redfish_password = args.redfish_password
#
# valid_include_config = ['all', 'cpu', 'bios','mempory']
# if include_config

obtained_metrics = ""
if 'all' in include_config:
    print(get_all(remote_host, redfish_username, redfish_password))
    exit(0)
else:
    if 'cpu' in include_config:
        print(get_cpu_attributes(remote_host, redfish_username, redfish_password))

    if 'memory' in include_config:
        print(get_memory_attributes(remote_host, redfish_username, redfish_password))

    if 'bios' in include_config:
        print(get_bios_settings(remote_host, redfish_username, redfish_password))

    if 'boot' in include_config:
        print(get_boot_attributes(remote_host, redfish_username, redfish_password))
