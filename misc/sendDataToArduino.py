import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600, timeout = 0.2)  
time.sleep(5)
print(ser.name)        
ser.write(bytes("Test", 'ascii'))
ser.close()    
