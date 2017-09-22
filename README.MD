D42 Required Field Notifier
===========================

What:
-----------
- D42 ReqFieldNot is a small flask API that integrates with a D42 instance, checking that each of a configurable set of fields are present and have a value.
- ReqFieldNot facilitates a webhook connection with a D42 instance and responds to new device events through HTTP POST.  
- ReqFieldNot then queries device's information from the D42 API and verifies that all the fields specified in your configuration are there.  
- If they are missing or aren't properly set, it notifies you through Slack.  


Why:
-------------
Have you ever encountered devices on your D42 Network that were missing critical information?  Fields can be empty or missing for a number of reasons.  ReqFieldNot will tell you when that happens.  


TODO:
------
- Integrate with Jira to create tickets whenever fields are missing for a new device.
- Tutorial write up.

Requirements:
--------------
Fully listed in requirements.txt but the main components right now are [Flask](http://flask.pocoo.org/) and [SlackClient](https://github.com/slackapi/python-slackclient)

Questions?
----------
Feel free to message me here on github and we can get connected through email. 
