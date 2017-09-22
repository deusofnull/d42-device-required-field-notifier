from flask import Flask, request
from checker import check_for_ip_fields
from alerter import alert_device_missing_fields
import json, requests

api_ip = 'https://10.42.2.117/api/1.0/'

app = Flask(__name__)


@app.route('/')
def home():
    return 'home'

@app.route('/new_webhook', methods=['GET', 'POST'])
def device_added():
    global api_ip
    if request.method == 'POST':
        response = json.loads(request.data)
        data = response['data']
        device_id = data['id']

        # get full device information from API
        # GET /api/1.0/devices/id/<device-id#>/

        device_id = data['id']
        url = api_ip + 'devices/id/%s/' % device_id
        res = requests.get(
            url,
            auth=('admin', 'adm!nd42'),
            headers={'Accept': 'application/json'},
            verify=False
        )

        device_data = json.loads(res.text)

        print 'device_data ' + str(device_data)

        if 'ip_addresses' in device_data:
            if len(device_data['ip_addresses']) > 0:
                for addr in device_data['ip_addresses']:
                    print '---*---'
                    missing = check_for_ip_fields(addr)
                    print 'missing fields: ' +  str(missing)
                    if len(missing) > 0:
                        print 'alert someone'
                        alert_device_missing_fields(device_id, missing)
            else:
                missing = 'no ip addresses exist'
                print 'alert someone'
                alert_device_missing_fields(device_id, missing)
        return 'got it'
    else:
        return 'POST only please'
