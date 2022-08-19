import subprocess
import serial
from uploadPhotoToDropbox import uploadPhotoToDropbox
ser = serial.Serial('/dev/ttyACM0',9600)

bastad = False #true if location is Båstad

while True:
	read_serial=ser.readline()
	if("Switch to Emergency" in read_serial):
		print("Message read!")
		s = subprocess.call(["fswebcam", "-r","3280x2464","/var/www/html/test.jpg"]) #TAKE PHOTO
		uploadPhotoToDropbox("/var/www/html/test.jpg") #UPLOAD TO DROPBOX - MAY NEED TO USE SUBPROCESS CALL 
		if(bastad): #SEND SMS
			s=subprocess.call(['./sendSMS.sh'])
		s=subprocess.call(["./stream.sh"]) #STREAM TO YOUTUBE
	print("---" + read_serial + "---")
