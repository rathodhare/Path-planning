
import sys
import serial

import time

try:
     ser = serial.Serial('/dev/ttyACM0',115200,timeout=1)
except serial.SerialException:
    try:
	ser = serial.Serial('/dev/ttyACM1',115200,timeout=1)
    except serial.SerialException:
        print (" You either aren't connected to port or see whether you used the correct open port or some port error")



while(True):
	file = open("/home/sine/rise_final_pp/final_can_.txt",'r') 
	#print file.readline()
	final_can_ = file.readline()
	print final_can_
	ser.write(final_can_)
