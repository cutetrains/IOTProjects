import sys
#import RPi.GPIO as GPIO
import os
from os.path import expanduser
from dotenv import load_dotenv
import time
from urllib.request import urlopen

load_dotenv(expanduser("~")+'\.env')
apiKey = os.getenv('api_key_thingspeak')

baseURL = 'http://api.thingspeak.com/update?api_key='+apiKey+'&field1='

while(True):
    x = input("Enter a number: ")
    html = urlopen(baseURL +str(x))
    print(html)
    time.sleep(15)
