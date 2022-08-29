import argparse


def parse_args(debug=False):
    parser = argparse.ArgumentParser(description='Get the BIOS configuration of the host.')
    parser.add_argument('--url', dest='host', default='http://localhost:9099',
                        help='URL of the redfish server. for eg. http://127.0.0.1')
    parser.add_argument('--username', dest='redfish_username', required=False,
                        help='Username to auth the redfish server')
    parser.add_argument('--password', dest='redfish_password', required=False,
                        help='Password to auth the redfish server.')
    parser.add_argument('--include', dest='include_configs', default='all',
                        choices=['cpu', 'memory', 'storage', 'nic', 'bios', 'boot', 'all'],
                        help='Fetch only specific settings'
                             'Defaults to all. valid values are cpu, memory, bios and all for now. '
                             'e.g. to get only cpu and memory metrics use --include="cpu"')
    parser.add_argument('--out-file', dest='output_file', required=False, help="Store metrics in the file")
    args = parser.parse_args()
    if debug:
        print(args)
    return args
