#!/usr/bin/env python
print "test"

import spidev
import time
import sys
import RPi.GPIO as GPIO
from array import *

#ads1220 registers
RREG  =   0x20
WREG  =   0x40
START =   0x08
STOP  =   0x0A
RDATAC=   0x10 
SDATAC	=	0x11	
RDATA	=	0x12

GPIO.setmode(GPIO.BOARD)

# Pin declararion
DRDY_PIN  = 13
START_PIN = 15
CS_PIN    = 18
RESET_PIN = 16

GPIO.setwarnings(False);

#Set pin direction
GPIO.setup(CS_PIN,GPIO.OUT)
GPIO.setup(DRDY_PIN,GPIO.IN)

spi = spidev.SpiDev()				# create spi object
spi.open(0,1)					# open spi port 0, device (CS)1
spi.max_speed_hz = (500000)
spi.mode = (1)

print "test"
count = 0

def Reg_Write(address,data):    # write Fibonacci series up to 
	print ("Writing %s to Register %s" %( hex(data),hex(address)))
	print(data);
    opcode1 = (address<<2) | 0x40

	GPIO.output(CS_PIN, False)
	time.sleep(0.002)               # sleep for 0.1 seconds
	GPIO.output(CS_PIN, True)
	time.sleep(0.002)               # sleep for 0.1 seconds

	GPIO.output(CS_PIN, False)
	time.sleep(0.002)               # sleep for 0.1 seconds
	resp = spi.xfer2([opcode1])        # transfer one byte
	resp = spi.xfer2([data])        # transfer one byte
	time.sleep(0.002)               # sleep for 0.1 seconds
	GPIO.output(CS_PIN, True)
	return;

def Reg_read(address):    # write Fibonacci series up to
	print ("Reading from Register %s" %(hex(address)))
        opcode1 = address | 0x20

        GPIO.output(CS_PIN, False)
        time.sleep(0.002)               # sleep for 0.1 seconds
        GPIO.output(CS_PIN, True)
        time.sleep(0.002)               # sleep for 0.1 seconds

        GPIO.output(CS_PIN, False)
        time.sleep(0.002)               # sleep for 0.1 seconds
        resp = spi.xfer2([opcode1])        # transfer one byte
        resp = spi.xfer2([0xff])        # transfer one byt
        time.sleep(0.002)               # sleep for 0.1 seconds
        GPIO.output(CS_PIN, True)

	#print("Data read is %s" %(hex(resp)))
	print(resp);
	return;

def Spi_command(command):    # write Fibonacci series up to
        GPIO.output(CS_PIN, False)
        time.sleep(0.002)               # sleep for 0.1 seconds
        GPIO.output(CS_PIN, True)
        time.sleep(0.002)               # sleep for 0.1 seconds

        GPIO.output(CS_PIN, False)
        time.sleep(0.002)               # sleep for 0.1 seconds
        resp = spi.xfer2([command])        # transfer one byte
        time.sleep(0.002)               # sleep for 0.1 seconds
        GPIO.output(CS_PIN, True)

        return;


def initialisation1():  
	print ("INITIALISATION");
	#GPIO.output(CS_PIN, False)


	Spi_command(START);				
	time.sleep(0.1);
	Spi_command(STOP);				
	time.sleep(0.1);

	Spi_command(SDATAC);				
	time.sleep(0.3);

	Reg_Write(0x00, 0x01); 		
	time.sleep(0.01); 
	Reg_Write(0x01, 0x04);	
	time.sleep(0.01); 
	Reg_Write(0x02, 0x10);		
	time.sleep(0.01); 
	Reg_Write(0x03, 0x00);	
	time.sleep(0.01); 
	
	Reg_read(0x00);
	time.sleep(0.1);
	Reg_read(0x04);
	time.sleep(0.1);
	Reg_read(0x08);
	time.sleep(0.1);
	Reg_read(0x0c);
	


        
	Spi_command(RDATAC);				
	time.sleep(0.3); 

	Spi_command(START);
	time.sleep(0.1);
	 

	GPIO.output(CS_PIN, True)
	return;


def toHex(dec):
	x = (dec % 16)
	digits = "0123456789ABCDEF"
	rest = dec / 16
	if (rest == 0):
		return digits[x]
	return toHex(rest) + digits[x]

def initialisation2():

	time.sleep(0.2)
	print "STARTED"

	#GPIO.output(CS_PIN, False)
	resp = spi.xfer2([0x11])        # transfer one byte
	time.sleep(0.3)	
	return;

def Read_Data():
	buff = [0,0,0,0,0,0,0,0,0];
	GPIO.output(CS_PIN, False)
	buff = spi.xfer2([0xff,0xff,0xff])
	GPIO.output(CS_PIN, True)
	
	print("0x %x %x %x\t"%(buff[0],buff[1],buff[2]))
	value = buff[0]<<16 | buff[1]<<8 | buff[2]
	print(value)
	volt = (float(value) * .000244140625)
        print  volt,"mV"
	return buff;
	#return r

def Read_adcvoltage():
	result = Read_Data()
	return result
	
	
voltage = 0

def ADCRead():
	#global voltage
	while(GPIO.input(DRDY_PIN) == True):
		time.sleep(0.001)		

	if (GPIO.input(DRDY_PIN) == False):
		#if 1:
		data = Read_adcvoltage();
		#val = ((data[5]&0xff) << 16) | ((data[6]&0xff) << 8) | (data[7]&0xff)
		val = ((data[6]&0xff) << 16) + ((data[7]&0xff) << 8) + (data[8]&0xff)
		#val = (data&0xff0000) + (data&0xff00) + (data&0xff)
		val = int(val)

		if( (val&(1<<(24-1))) != 0 ):
			value = val - 0x1000000			
		else:
			value = val
			
		voltage = (float(value)*100/8388607)
	return voltage	


while True:

	Read_Data()
	time.sleep(0.5)