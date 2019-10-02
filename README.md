# MoistureAlert

Using a Raspberry Pi, a Capacitive Moisture Sensor, and a PCF8591T ADC, MoistureAlert informs planters/farmers when the soil level is too low and the plants must be watered.  

This program is written using Python and smbus with the RPi GPIO library. The program takes in readings from the moisture sensor when the levels are below a certain threshold (based on research for the plant used to test), the user is alerted through a connected LCD (for onsite checks) and through telemetry sent to the Azure IoT Hub (for offsite checks). Messages and detections are within 1 second of accuracy as Azure IoT Hub only allows for a certain amount of messages sent a day (on a free subscription). 

As for the hardware, the capacitive moisture sensor is connected to a PCF8519T ADC, then connected to a Raspberry Pi as an I2C device. The LCD is connected to the Raspberry Pi, also as an I2C device. 

# Currently broken features
- Sending telemetry through the Azure IoT Hub
  - This is due to my Azure account not having sufficient funds (I'm broke)
  - However, all features should work, if needed to be tested, please create your own Azure IoT Hub and replace the connection
    string with your own

# Incoming features
- Reporting data and alerts to a mobile app
- User defined moisture levels
