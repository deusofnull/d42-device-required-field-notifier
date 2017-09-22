import os
from slackclient import SlackClient

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slackClient = SlackClient(SLACK_TOKEN)

def alert_device_missing_fields(device_id, missing):
    msg = "missing fields on new device %s : %s" % (device_id, missing)
    slackClient.api_call(
        "chat.postMessage",
        channel='#logs',
        text=msg
    )
    return 'posted'
