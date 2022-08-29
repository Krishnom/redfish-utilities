import argparse
import redfish
import json

import utils.commons


def is_response_ok(status):
    return int(status) < 400

def get_all(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str
def get_bios_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/Bios/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str

def get_cpu_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/Processors/Settings"
    context = f"/redfish/v1/Systems/{system_id}/ProcessorSummary/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str

def get_memory_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/Memory/Settings"
    context = f"/redfish/v1/Systems/{system_id}/MemorySummary/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str

def get_nic_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/EthernetInterfaces/Settings"
    context = f"/redfish/v1/Systems/{system_id}/NetworkInterfaces/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str
def get_storage_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/Storage/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str

def get_boot_settings(redfish_url, username=None, password=None, system_id=1):
    context = f"/redfish/v1/Systems/{system_id}/BootOptions/Settings"
    j_str = json.loads(fire_redfish_api(redfish_url, username=username, password=password, context=context))
    print(j_str)
    return j_str


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
args = utils.commons.parse_args(debug=True)
remote_host = args.host
include_config = [inc.strip() for inc in str(args.include_configs).split()]
redfish_username = args.redfish_username
redfish_password = args.redfish_password
#
# valid_include_config = ['all', 'cpu', 'bios','mempory']
# if include_config


print('---------------------------------------------------------------------------------------------')
obtained_metrics = ""
if 'all' in include_config:
    obtained_metrics = get_all(remote_host, redfish_username, redfish_password)
    print(obtained_metrics)
else:
    if 'cpu' in include_config:
        print(get_cpu_settings(remote_host, redfish_username, redfish_password))

    if 'memory' in include_config:
        print(get_memory_settings(remote_host, redfish_username, redfish_password))

    if 'bios' in include_config:
        print(get_bios_settings(remote_host, redfish_username, redfish_password))

    if 'boot' in include_config:
        print(get_boot_settings(remote_host, redfish_username, redfish_password))

    if 'storage' in include_config:
        print(get_storage_settings(remote_host, redfish_username, redfish_password))

    if 'nic' in include_config:
        print(get_nic_settings(remote_host, redfish_username, redfish_password))
print('---------------------------------------------------------------------------------------------')
