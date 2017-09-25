from flask import Flask, request
from checker import *
from alerter import alert_device_missing_fields
import json, requests, os, logging

api_ip = os.environ.get('D42_API_IP')
logging.basicConfig(filename='service.log',level=logging.WARNING)

app = Flask(__name__)

req_fields = {}
req_fields['ip_addresses'] = ['ip', 'macaddress', 'subnet', 'subnet_id', 'type']
req_fields['name'] = []


# get full device information from API
# GET /api/1.0/devices/id/<device-id#>/
def get_device(device_id):
    global api_ip
    url = api_ip + 'devices/id/%s/' % device_id
    try:
        res = requests.get(
            url,
            auth=('admin', 'adm!nd42'),
            headers={'Accept': 'application/json'},
            verify=False # https call to localhost requires skipping verification
        )
        return res
    except Exception as e:
        logging.exception("Error")
        return e

@app.route('/new_device', methods=['POST'])
def device_added():
    if request.method == 'POST':
        req = json.loads(request.data)
        data = req['data']
        device_id = data['id']

        res = get_device(device_id)

        device_data = json.loads(res.text)

        check_result = check_ip_mac(device_data, device_id)
        return str(check_result)

    else:
        return 'POST only please'

@app.route('/check_device', methods=['POST'])
def check_device():
    device_data = json.loads(request.data)
    device_id = device_data['id']


    check_result = check_ip_mac(device_data, device_id)
    return str(check_result)
