import json
from alerter import alert_device_missing_fields

'''
checker provides basic checking functions for the ip addresses and mac addresses
of a d42 device.
TODO: create recursive checking functions that would allow for checking of
arbitrary depth fields.

a valid IP addresses would look like
"ip_addresses": [
        {
            "ip": "192.168.0.1",
            "label": "testlabel",
            "macaddress": "example.mac.address",
            "subnet": "Infra-10.1.10.0/24(Infrastructure Services)",
            "subnet_id": "42",
            "type": 1
        }
    ]

a valid mac addresses would look like
 "mac_addresses": [
        {
            "mac": "00:11:22:33:44:55",
            "port": "FastEthernet0/4 @ nh-lab-switch-01",
            "port_name": "",
            "vlan": null
        }
    ]
'''

def check(field, addr):
    print addr[field]
    return True if field in addr and addr[field] else False

def check_for_fields(addr, required_fields, addr_type, index):

    # checked is a bool array with the same size of required_fields
    # if an element of checked is false, that IP field or value is missing
    # ie. if ip was empty string, checked = [False, True, True, True, True]
    checked = [check(i, addr) for i in required_fields]

    missing_field_idx = []
    if False in checked:
        for (key, val) in enumerate(checked):
            if val == False:
                missing_field_idx.append(key)

    # simple way of getting field names
    missing_field_names = []
    for miss in missing_field_idx:
        # print '%s field is missing ' % required_fields[miss]
        missing_field_names.append('%s[%i].%s' % (addr_type, index, required_fields[miss]) )

    return missing_field_names

def check_for_ip_addrs(device_data, device_id):
    if 'ip_addresses' in device_data:
        check_result = check_each_ip_addr(device_data['ip_addresses'], device_id)
        return check_result
    else:
        missing = 'No ip_addresses field exists.'
        alert_device_missing_fields(device_id, missing)
        return missing


def check_each_ip_addr(ip_addresses, device_id):
    required_fields = ['ip', 'macaddress', 'subnet', 'subnet_id', 'type']

    if len(ip_addresses) > 0:
        index = 0
        for addr in ip_addresses:
            print '---*---'
            missing = check_for_fields(addr, required_fields, 'ip_addresses', index)
            print 'missing fields: ' +  str(missing)
            if len(missing) > 0:
                print 'alert someone'
                alert_device_missing_fields(device_id, missing)
                return missing
            index += 1
            return 'All fields accounted for'
    else:
        missing = 'No IP Addresses Exist'
        print 'alert someone'
        alert_device_missing_fields(device_id, missing)
        return missing


def check_for_mac_addrs(device_data, device_id):
    if 'mac_addresses' in device_data:
        check_result = check_each_mac_addr(device_data['mac_addresses'], device_id)
        return check_result
    else:
        missing = 'No mac_addresses field exists.'
        alert_device_missing_fields(device_id, missing)
        return missing


def check_each_mac_addr(mac_addresses, device_id):
    required_fields = ['mac', 'port']

    if len(mac_addresses) > 0:
        index = 0
        for addr in mac_addresses:
            print '---*---'
            missing = check_for_fields(addr, required_fields, 'mac_addresses', index)
            print 'missing fields: ' +  str(missing)
            if len(missing) > 0:
                print 'alert someone'
                alert_device_missing_fields(device_id, missing)
                return missing
            index += 1
            return 'All fields accounted for'
    else:
        missing = 'No Mac Addresses Exist'
        print 'alert someone'
        alert_device_missing_fields(device_id, missing)
        return missing

def check_ip_mac(device_data, device_id):
    check_results = []
    check_results.append(check_for_ip_addrs(device_data, device_id))
    check_results.append(check_for_mac_addrs(device_data, device_id))
    return check_results
