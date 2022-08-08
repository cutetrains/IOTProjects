# IOTProjects
A common repository for IOT projects

The code needs a `.env` file in the home folder that contains secret information such as API keys and passwords.
```
api_key = abc123
password = Your_Password`
```

## uploadDropbox
Uploads a file to Dropbox/apps/appName. 

`python misc/uploadDropbox.py <fileName>`

## sendSMS
Sends a predefined text message

`python misc/sendSMS.py`

TODO: Make the file accept parameters for phone number and message
