#!/usr/bin/env python3
# Filename: MoistureAlert.py
# Author: Kenny Yu
# Date: 8/13/19
# Sources of help/guidance: Freenove Kit, Sparkfun, PCF8574 and PCF8591 manuals

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

import smbus
import time

address = 0x48	# default address of PCF8591
bus = smbus.SMBus(1) # Initializes IC Bus
cmd = 0x40

PCF8574_address = 0x27 # The I2C address of PCF8574T

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
# Function Description: Delegates to analogRead to read value, then displays
#     the value that was read in onto the LCD connected
# Parameters: None
# Side Effects: Displays the ADC Value on an LCD
# Return Value: None
def readValue():
	# Turn on LCD backlight
	mcp.output( 3, 1 )
	lcd.begin( 16, 2 )

	while True:
		# Read and print value at channel zero
		value = analogRead( 0 )	

		# Display the value
		lcd.setCursor( 0, 0 )
		lcd.message( 'Moisture: %d' % ( value ) + '\n' )
		if value > 200: 
			lcd.message( 'Please water!' + '\n' )
		elif value <= 200:
			lcd.message( 'Still good :D' + '\n' )
		time.sleep( 0.01 )

# Function Name: end()
# Function Description: Releases the bus(es) after program finishes, so they
#     can be used again
# Parameters: None
# Side Effects: Releases the bus
# Return Value: None
def end():
	lcd.clear()
	bus.close()	

# Create PCF8574 GPIO adapter
try: 
	mcp = PCF8574_GPIO( PCF8574_address )
except: 
	print ( 'I2C Address Error!' )
	exit(1)

# Create LCD passing in GPIO adapter
lcd = Adafruit_CharLCD( pin_rs = 0, pin_e = 2, pins_db = [4,5,6,7], GPIO = mcp )
	
if __name__ == '__main__':
	try:
		readValue()

	# If Ctrl + C is entered
	except KeyboardInterrupt:
		end()
		
	
