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
Sends a text message using a TP-link MR600 router and a js script from https://github.com/plewin/tp-link-modem-router

`python misc/sendSMS.py 01234567890 "Lorem ipsum dolor sit amet"`
