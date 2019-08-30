#!/usr/bin/env python3
# Filename: MoistureAlert.py
# Author: Kenny Yu
# Date: 8/13/19
# Sources of help/guidance: Freenove Kit, Sparkfun, PCF8574 and PCF8591 manuals

from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD

import smbus
import time
import random
import config as config
import iothub_client

from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue
from telemetry import Telemetry

# Choose MQTT as protocol
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000

# IoT Hub Connection String
CONNECTION_STRING = "HostName=Learner.azure-devices.net;DeviceId=thepimistake;SharedAccessKey=TZe/FEf3cowtfxHIsI8e/I+UbNhRnmS7fl3ktlYt/L4="

# Define JSON message to send to IoT Hub
MSG_TXT = "{\"moisture\": %d}"

# Default address of PCF8591
address = 0x48

# Initializes IC Bus
bus = smbus.SMBus(1)
cmd = 0x40

# The I2C address of PCF8574T
PCF8574_address = 0x27

# Function Name: initHub()
# Function Description: Initialize the IoT hub
# Parameters: None
# Side Effects: Connects to the hub using the connection string and 
#     clarifies protocol
# Return Value: The client
def initHub(): 
	# Create an IoT Hub client
	client - IoTHubClient( CONNECTION_STRING, PROTOCOL )
	return client

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

	# Try to init client and send messages
	try: 
		client = iothub_client_init()
		print ( "IoT device sending messages, press Ctrl+C to exit" )

		while True:
			# Read and print value at channel zero
			value = analogRead( 0 )	

			# Display the value
			lcd.setCursor( 0, 0 )
			lcd.message( 'Moisture: %d' % ( value ) + '\n' )
			if value > 200: 
				lcd.message( 'Please water!' + '\n' )
				msg_txt = MSG_TXT % ( value )
			elif value <= 200:
				lcd.message( 'Still good :D' + '\n' )
				msg_txt = MSG_TXT % ( value )
			message = IoTHubMessage( msg_txt )

			# Send message
			print ( "Sending message: %s" % message.get_string() )
			client.send_event_async( message, 
			    send_confirmation_callback, None)
			time.sleep( 1 )

	except IoTHubError as iothub_error:
		print ( "Unexpected error %s from IoTHub" % iothub_error )
		return 
			
# Function Name: end()
# Function Description: Releases the bus(es) after program finishes, so they
#     can be used again
# Parameters: None
# Side Effects: Releases the bus
# Return Value: None
def end():
	lcd.clear()
	bus.close()	
	print ( "IoTHubClient stopped" )

# Create PCF8574 GPIO adapter
try: 
	mcp = PCF8574_GPIO( PCF8574_address )
except: 
	print ( 'I2C Address Error!' )
	exit(1)

# Create LCD passing in GPIO adapter
lcd = Adafruit_CharLCD( pin_rs = 0, pin_e = 2, pins_db = [4,5,6,7], GPIO = mcp )

# Main function that calls everything
if __name__ == '__main__':
	try:
		readValue()

	# If Ctrl + C is entered
	except KeyboardInterrupt:
		end()
		
	
