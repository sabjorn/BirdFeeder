import Adafruit_BBIO.GPIO as GPIO #GPIO
import time
import sys

class Ultrasonic:
	def __init__(self, trig, echo, thresh_low, thersh_high):
		""" Initiate ultrasonic Range """
		self.echo = echo
		self.trig = trig
		self.thresh_low = thresh_low
		self.thresh_high = thresh_high
		
		self.hist_flag = 0 #historesis flag
		self.dist = 0 #distance storage


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
		GPIO.output(self.trig, GPIO.LOW)

		while GPIO.input(self.echo)==0:
			pass
		pulse_start = time.time()
		while GPIO.input(self.echo)==1:
			pass
		pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		dist = pulse_duration * 17150
		self.dist = round(dist, 2)

		return self.dist

	def threshold(self):
		if self.distance() < self.thresh_low:
			return 1
		else:
			return 0

	#if the value is below the thesh_low, flag HIGH.
	# once this flag is HIGH, if the value goes above thresh_high, flag LOW
	def hyst(self):
		if (self.distance() < self.thresh_low and not self.hist_flag):
			self.hist_flag = 1
		elif (self.distance > self.thresh_high and self.hist_flag):
			self.hist_flag = 0

		return self.hist_flag

	def close(self):
        	""" Graceful shutdown """ 
        	GPIO.cleanup()