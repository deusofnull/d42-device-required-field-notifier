D42 Required Field Notifier
===========================

What:
-----------
- D42 ReqFieldNotifier is a small flask API that integrates with a D42 instance, checking that each of a configurable set of fields are present and have a value.
- ReqFieldNotifier facilitates a webhook connection with a D42 instance and responds to new device events through HTTP POST.  
- ReqFieldNotifier then queries device's information from the D42 API and verifies that all the fields specified in your configuration are there.  
- If they are missing or aren't properly set, it notifies you through Slack.  


Why:
-------------
Have you ever encountered devices on your D42 Network that were missing critical information?  Fields can be empty or missing for a number of reasons.  ReqFieldNotifier will tell you when that happens.  

How:
-------
- Create Webhook Action in Device 42 under Tools > Webhook > Actions. Chose the "Device" category and select Process Change and Add Events.
- Create Webhook endpoint and point it towards the IP running ReqFieldNotifier, for example: 192.168.0.1:5000/new_device
- [Create a new Slack App](https://api.slack.com/slack-apps#creating_apps) and [install it](https://api.slack.com/slack-apps#installing_apps) to your slack server.  Make sure the channel you are posting to exists, in the default configuration, a channel '#logs' is used.

TODO:
------
- Integrate with Jira to create tickets whenever fields are missing for a new device.
- Tutorial write up.
- Create Recursive field checker that allows for arbitrary depth checking.  


Requirements:
--------------
Fully listed in requirements.txt but the main components right now are [Flask](http://flask.pocoo.org/) and [SlackClient](https://github.com/slackapi/python-slackclient)

Questions?
----------
Feel free to message me here on github and we can get connected through email.
