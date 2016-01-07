import Adafruit_BBIO.GPIO as GPIO #GPIO
from goprohero import GoProHero #goPro
from ultrasonic import Ultrasonic
import time

#members
LED = 'P9_16' #LED to show status
#TRIG = 'P9_12' #trigger pin on ultrasonic
#ECHO = 'P9_14' #echo pin receieve

pulse_start = 0
pulse_end = 0
thresh = 10. #distance threshold for ultrasonic 
status_flag = 0 #within threshold value
val = 0

#setup
#GPIO.setup(ECHO, GPIO.IN)
#GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)

camera = GoProHero(password='r00ba770') #connect to camera
#=========================================================

while(1):
	try:
		# GPIO.output(TRIG, GPIO.LOW)
  #       	time.sleep(.5) #let settle

  #       	GPIO.output(TRIG, GPIO.HIGH)
  #       	time.sleep(0.00001)
  #       	GPIO.output(TRIG, GPIO.LOW)

  #       	while GPIO.input(ECHO)==0:
  #               	pass
  #       	pulse_start = time.time()
  #       	while GPIO.input(ECHO)==1:
  #       		pass
		# pulse_end = time.time()
		
  #               pulse_duration = pulse_end - pulse_start
		# distance = pulse_duration * 17150
		# distance = round(distance, 2)
		# print distance	
		# if(distance < thresh):
		# 	status_flag = 1
		# 	val = GPIO.HIGH
		# else:
		# 	status_flag = 0
		# 	val = GPIO.LOW
		
		GPIO.output(LED, val)
		status = camera.status()
		if(status_flag == 1 and status['record'] != 'on'):
			camera.command('record','on')
			#print('recording')
		elif(status['record'] != 'off' and status_flag == 0):
			camera.command('record','off')
	except KeyboardInterrupt:
		GPIO.cleanup()
		camera.command('record','off')
		raise
	except:
		print("You need to run as ROOT asshole")
		exit(-1)
