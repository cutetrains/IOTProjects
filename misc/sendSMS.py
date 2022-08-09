import subprocess
import os
from os.path import expanduser
from dotenv import load_dotenv
import sys
#https://github.com/plewin/tp-link-modem-router

#Script not tested on RPI on network with TP-link 4G router yet

load_dotenv(expanduser("~")+'\.env')
ip_TPLink = os.getenv('ip_TPLink')
user_TPLink = os.getenv('user_TPLink')
password_TPLink = os.getenv('password_TPLink')

if(len(sys.argv) == 1):
    print("No parameters specified, using phone number from .env and test2 as message.")
    phone_number = os.getenv('phone_number')
    message = "test2"

elif(len(sys.argv) == 3):
    phone_number = sys.argv[1]
    message  = sys.argv[2]
else:
     print("Usage:")
     print("python sendSMS.py")
     print('python sendSMS.py 01234567890 "Lorem ipsum dolor sit amet"')
     sys.exit()
#message = "Stream started from RPI. URL: https://www.youtube.com/channel/UC1lDhijDvNyHWC1y4KuR0Iw/live"

print(f'cd /var/www/html/plugins/script/data/tp-link-modem-router/; ./sms-send.js --url="http://{ip_TPLink}" --login="{user_TPLink}" --password="{password_TPLink}" "{phone_number}" "{message}"; cd ~/sandbox/ ')

cmdList = ['cd', '/var/www/html/plugins/script/data/tp-link-modem-router/;', './sms-send.js','--url="http://' +ip_TPLink + '"', '--login="'+user_TPLink + '"', '--password="'+password_TPLink+'"', '"'+phone_number+'"', '"' +message + '";', 'cd', '~/sandbox']
print(cmdList)

s=subprocess.call(cmdList)
