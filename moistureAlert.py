# Filename: moistureAlert.py
# Description: Reads in the data from the capacitive moisture sensor
# Author: Kenny Yu
# Date: 8/9/19

# Import the Raspberry Pi GPIO library 
import RPi.GPIO as GPIO

moisturePin = 40	# define the pin for the moisture sensor

# Function Name: setup() 
# Function Description: Sets GPIO21/pin 40 as an input pin 
# Parameters: None
# Return Value: None
def setup():
	print ( 'Program is starting...' )
	GPIO.setmode( GPIO.BOARD )	# Numbers GPIO by physical location
	GPIO.setup( moisturePin, GPIO.IN )	# Sets the sensor as input

# Function Name: inputOutput()
# Function Description: Prints the readings from soil sensor
# Parameters: None
# Return Value: None
def inputOutput():
	print ( GPIO.input(moisturePin) )	# Prints sensor reading

# Function Name: destroy()
# Function Description: Runs when the program ends to release resources
#     using GPIO's cleanup function
# Parameters: None
# Return Value: None
def destroy():  
	GPIO.cleanup()	

if __name__ == '__main__':	# Program start
	setup()
	try:
		inputOutput()
	except KeyboardInterrupt:	# Ctrl+C will stop running program
		destroy()
