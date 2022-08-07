import subprocess

#https://github.com/plewin/tp-link-modem-router

#Script not tested on RPI on network with TP-link 4G router yet
import os
from os.path import expanduser
from dotenv import load_dotenv

load_dotenv(expanduser("~")+'\.env')

ip_TPLink = os.getenv('ip_TPLink')
user_TPLink = os.getenv('user_TPLink')
password_TPLink = os.getenv('password_TPLink')
phone_number = os.getenv('phone_number')

message = "Stream started from RPI. URL: https://www.youtube.com/channel/UC1lDhijDvNyHWC1y4KuR0Iw/live"

print(f'cd /var/www/html/plugins/script/data/tp-link-modem-router/; ./sms-send.js --url="http://{ip_TPLink}" --login="{user_TPLink}" --password="{password_TPLink}" "{phone_number}" "{message}"; cd ~/sandbox/ ')

cmdList = ['cd', '/var/www/html/plugins/script/data/tp-link-modem-router/;', './sms-send.js','--url="http://' +ip_TPLink + '"', '--login="'+user_TPLink + '"', '--password="'+password_TPLink+'"', '"'+phone_number+'"', '"' +message + '";', 'cd', '~/sandbox']
print(cmdList)

s=subprocess.call(cmdList)

