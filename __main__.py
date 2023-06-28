
from __future__ import division
import time
import Adafruit_PCA9685
from picamera import PiCamera
import os
import json
import Camera
import ServicesAPI




pwm = Adafruit_PCA9685.PCA9685()

nomeServo = ""

# Camera object context
cam = Camera.Camera()
cam.configure()

serv = [0,4,8,12,15]
value = [375, 500, 500, 210, 450]
order = [2,1,0,3,4]
inicio = [1,2,0,4,3]


# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
    
def arm_position():
	
	value = [375, 500, 500, 210, 450]
	#raw_input()
	#Clear
	#os.system('clear')
	# Abrindo Preview da camera
	#if(Openflag == False):
		#camera.start_preview(fullscreen=False, window=(800,000,640,480))
	for j in range(320):
		if((j)%20 == 0 and j!=0):
			value[1] = 500
			for i in range(data[j-1]["1"], 500):
				pwm.set_pwm(serv[1], 0, i)
				time.sleep(0.01)
			time.sleep(5)
			value[2] = 400
			for i in range(data[j-1]["2"], 400, -1):
				pwm.set_pwm(serv[2], 0, i)
				time.sleep(0.01)
			time.sleep(10)
		
		for k in order:
			antes = value[k]
			value[k] = data[j][str(k)]
			if(antes != value[k]):
				if(k == 1):
					for i in range(antes, 550):
						pwm.set_pwm(serv[k], 0, i)
						time.sleep(0.01) 
					for i in range(550, value[k], -1):
						pwm.set_pwm(serv[k], 0, i)
						time.sleep(0.01)
				else:
					if value[k] > antes:
						for i in range(antes, value[k]):
							pwm.set_pwm(serv[k], 0, i)
							time.sleep(0.01)
					else:
						for i in range(antes, value[k], -1):
							pwm.set_pwm(serv[k], 0, i)
							time.sleep(0.01)
				if (k==3 or k==4):
					time.sleep(1)
				else:
					time.sleep(3)
		#Codigo para Tirar Foto
		cam.startPlateCapture(j)
		





		#time.sleep(3)
		#print(j)
	value = [375, 500, 500, 210, 450]
	for k in inicio:
		antes = data[319][str(k)]
		if value[k] > antes:
			for i in range(antes, value[k]):
				pwm.set_pwm(serv[k], 0, i)
				time.sleep(0.01)
			else:
				for i in range(antes, value[k], -1):
					pwm.set_pwm(serv[k], 0, i)
					time.sleep(0.01)
		time.sleep(5)   
    
# Function for the print values
	

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)


count = 0
var_exit = 0

# Initial Position
f = open('/home/pi/Desktop/Planilha.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close()
for i in inicio:
		pwm.set_pwm(serv[i], 0, int(value[i]))
		time.sleep(5)


		
while(1):
	arm_position()
	#Upload das fotos para o TrapSystem
		



	
		
		
