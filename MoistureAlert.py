#!/usr/bin/env python3
# Filename: MoistureAlert.py
# Author: Kenny Yu
# Date: 8/13/19
import smbus
import time

address = 0x48	# default address of PCF8591
bus=smbus.SMBus(1) # Initializes IC Bus
cmd=0x40		#command

# Function Name: analogRead()
# Function Description: Read the ADC value from the channel that was 
#     passed in
# Parameters: chn - the channel where the sensor/device is connected to
# Side Effects: None
# Return Value: The value the sensor is outputting
def analogRead(chn):
	value = bus.read_byte_data(address,cmd+chn)
	return value

# Function Name: readValue()
# Function Description: Delegates to analogRead to read value, then prints
#     the value that was read in
# Parameters: None
# Side Effects: Prints the ADC Value
# Return Value: None
def readValue():
	while True:
		value = analogRead(0)	# read value at channel 0
		print ('Moisture Level: %d'%(value))
		time.sleep(0.01)

# Function Name: end()
# Function Description: Releases the bus(es) after program finishes, so they
#     can be used again
# Parameters: None
# Side Effects: Releases the bus
# Return Value: None
def end():
	bus.close()
	
if __name__ == '__main__':
	try:
		readValue()

	# If Ctrl + C is entered
	except KeyboardInterrupt:
		end()
		
	
