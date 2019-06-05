# blink LED every 1 second
import machine 			# the machine module hols the pin configurations and modes.
from time import sleep  			# import sleep for some delay
led_pin = 5					# connect led to GPIO5 = 
LED = machine.Pin(led_pin, machine.PIN.OUT)	# configure LED as OUTPUT
while True:					# run forever
    LED.value(1)				# set LED to HIGH
    sleep(1)					# wait 1 second
    LED.value(0)				# set LED to LOW
    sleep(0)					# wait 1 second
