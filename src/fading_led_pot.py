# Fading LED every 0.5 by reading data from Potentiometer
import machine		
from time import sleep
led_pin = 5     			# led pin
pot_pin = 0				# ADC0 pin 
LED = machine.PIN(led_pin)		# create LED object 
LED_pwm = machine.PWM(LED, freq=500) # create LED_pwm object and set frequency to 500Hz
while True:				
    LED_pwm.duty(pot_pin.read()) # get the value from the Pot and set it to the duty cycle 
    sleep(0.5)				# wait 0.5
