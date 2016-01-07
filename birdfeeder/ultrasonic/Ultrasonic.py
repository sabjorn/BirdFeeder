import Adafruit_BBIO.GPIO as GPIO #GPIO
import time
import sys

class Ultrasonic:
    def __init__(self, trig, echo):
        """ Initiate ultrasonic Range """ 
        self.echo = echo
        self.trig = trig

        self.distance = 0
        
        ##setup GPIO
        GPIO.setup(self.echo, GPIO.IN)
		GPIO.setup(self.trig, GPIO.OUT)


    def distance(self):
        """ Return distance from Ultrasonic Range Finder """
        pulse_start = 0
        pulse_end = 0

        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(.5) #let settle
        GPIO.output(self.trig, GPIO.HIGH)
        time.sleep(0.00001)
    	GPIO.output(TRIG, GPIO.LOW)

    	while GPIO.input(self.echo)==0:
            pass
    	pulse_start = time.time()
    	while GPIO.input(self.echo)==1:
    		pass
		pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		self.distance = round(distance, 2)

		return self.distance


    def close(self):
        """ Graceful shutdown """ 
        GPIO.cleanup()