import Adafruit_BBIO.GPIO as GPIO #GPIO
from goprohero import GoProHero #goPro
from ultrasonic import Ultrasonic
import time

#members
LED = 'P9_16' #LED to show status
TRIG = 'P9_12' #trigger pin on ultrasonic
ECHO = 'P9_14' #echo pin receieve

pulse_start = 0
pulse_end = 0
thresh = 20. #distance threshold for ultrasonic 
status_flag = 0 #within threshold value
val = 0

#setup
GPIO.setup(LED, GPIO.OUT)

rangefinder = Ultrasonic(TRIG, ECHO)
camera = GoProHero(password='r00ba770') #connect to camera
#=========================================================

while(1):
	try:
		distance = rangefinder.distance()
		if(distance < thresh):
			status_flag = 1
			val = GPIO.HIGH
		else:
			status_flag = 0
			val = GPIO.LOW
		
		GPIO.output(LED, val)
		status = camera.status()
		if(status_flag == 1 and status['record'] != 'on'):
			camera.command('record','on')
			#print('recording')
		elif(status['record'] != 'off' and status_flag == 0):
			camera.command('record','off')
	except KeyboardInterrupt:
		GPIO.cleanup()
		rangefinder.close()	
		camera.command('record','off')
		raise
	except:
		print("You need to run as ROOT asshole")
		exit(-1)
