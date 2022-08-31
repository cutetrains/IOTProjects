#!/usr/bin/env python
# This script will be used along with Playknowingly Robot
# https://www.kjell.com/se/produkter/hem-fritid/lek-lar/programmerbara-robotar/playknowlogy-arduino-robotbil-startpaket-p87288
#
#Updated Arduino code:
# https://create.arduino.cc/editor/f98gb/2c9678b8-8141-47ab-b253-4b8587fc57cb/preview

import time
import serial
import sys
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0.050)
#ser = serial.Serial('COM4', 9600, timeout=0.050)
count = 0

while 1:
    name = raw_input()
    print(name)
    s = name+'\n'
    #print("Sending" + "A\n")
    ser.write(s.encode())
    #time.sleep(5)
    count += 1
