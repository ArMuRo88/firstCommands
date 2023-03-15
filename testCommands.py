import easygui
from easygui import *

import serial
import array as arr
from time import sleep

ser = serial.Serial("/dev/ttyS0")
ser.baudrate = 9600

print ("Start")
userData = input("Command: ")

ser.write(bytearray(userData,'ascii'))
i = 0
data = ''

while True:
        word = ser.read()
             
        i = i + 1
        data += word.decode('ascii')
           
        if (word == bytes('#','ascii')):
            print(i)            
            i = 0
            print(data)
            data = ''
            userData = input("Command: ")
            ser.write(bytearray(userData,'ascii'))
        #print(word)