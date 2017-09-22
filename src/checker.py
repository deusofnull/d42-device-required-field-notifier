import json


def check(field, ip):
    print ip[field]
    return True if field in ip and ip[field] else False

def check_for_ip_fields(ip):
    print 'check_for_ip_fields'
    required_fields = ['ip', 'macaddress', 'subnet', 'subnet_id', 'type']

    # checked is a bool array with the same size of required_fields
    # if an element of checked is false, that IP field or value is missing
    # ie. if ip was empty string, checked = [False, True, True, True, True]
    checked = [check(i, ip) for i in required_fields]

    missing_field_idx = []
    if False in checked:
        for (key, val) in enumerate(checked):
            if val == False:
                missing_field_idx.append(key)
    # print 'missing fields' + str(missing_field_idx)

    # this is just a messy way to get the names of the missing fields
    missing_field_names = []
    for miss in missing_field_idx:
        # print '%s field is missing ' % required_fields[miss]
        missing_field_names.append(required_fields[miss])

    return missing_field_names
