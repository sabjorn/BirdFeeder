import Adafruit_BBIO.GPIO as GPIO #GPIO
from goprohero import GoProHero #goPro
from ultrasonic import Ultrasonic
import time
import os

filename = 'audio.wav' #sound file

#members
LED = 'P9_16' #LED to show status
TRIG = 'P9_12' #trigger pin on ultrasonic
ECHO = 'P9_14' #echo pin receieve

thresh = 20. #distance threshold for ultrasonic 
status_flag = 0 #within threshold value
val = 0

#setup
GPIO.setup(LED, GPIO.OUT)

rangefinder = Ultrasonic(TRIG, ECHO, thresh)
camera = GoProHero(password='r00ba770') #connect to camera
#=========================================================

while(1):
	try:
		status_flag = rangefinder.threshold()
		
		GPIO.output(LED, status_flag)
		status = camera.status()
		if(status_flag == 1 and status['record'] != 'on'):
			camera.command('record','on')
			os.system('aplay ' + filename)
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
