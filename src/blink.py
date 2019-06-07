# blink LED every 1 second
def blink(pin=5, time=1):		# blink function by default pin = 5, time = 1 you can change it
    import machine 			# the machine module holds the pin configurations and modes.
    from time import sleep  		# import sleep for some delay				
    LED = machine.Pin(pin, machine.Pin.OUT)	# configure LED as OUTPUT
    while True:			# run forever
        LED.value(1)			# set LED to HIGH
        sleep(time)			# wait 1 second by default
        LED.value(0)			# set LED to LOW
        sleep(time)			# wait 1 second by default
