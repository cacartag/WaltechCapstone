import serial
import sys
import time
import tester
import datetime
import time
import subprocess

from subprocess import PIPE
#purpose of this class is to Communicate with the Arduino serially 

class SerialCommunicator():

    def __init__(self,PortNumber):
        #setup for serial communication
        self.ser = serial.Serial(
            port=PortNumber,
            baudrate=9600,
            stopbits=1,
            bytesize=serial.EIGHTBITS)
            
        #needed to finish the setup
        time.sleep(1)
       
       
    #gets the state of the arduino        
    def getArduinoState(self):
        
        self.ser.write("ready")
        
        bytes = self.ser.inWaiting();        #checks how many bytes are in input buffer
        
        while bytes < 13:                    #waits till there is more than 12 bytes
            
            self.ser.reset_input_buffer()    #when put together it flushes everything
            received = self.ser.read(13)     #but the read size
            
            return received
        
        
se = SerialCommunicator("com4")

print se.getArduinoState()