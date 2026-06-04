
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep


#Servo Default Positions
shoulderAngle = 20
elbowAngle = 40
wristAngle = 90
clawAngle = 103
camAngle = 90

PWM = 50 #PWM frequency to 50hz (standard value for servo)

#Initialize I2C bus using busio
i2c = busio.I2C(SCL, SDA)

#Create a simple PCA9685 class instance for the Servo Driver
pca = PCA9685(i2c, address=0x5f) #default 0x40 but HAT uses 0x5f
pca.frequency = PWM

class robotServo:
	def __init__(self, pin, angle, minAngle = 10, maxAngle = 180):
		self.pin = pin
		self.angle = angle
		self.minAngle = minAngle
		self.maxAngle = maxAngle
		
	def setServoAngle(self):
		#Intialize servo & set angle
		servoAngle = servo.Servo(pca.channels[self.pin], min_pulse=200, max_pulse=2400, actuation_range=180)
		if self.angle < self.minAngle:
			self.angle = self.minAngle
		if self.angle > self.maxAngle:
			self.angle = self.maxAngle
		servoAngle.angle = self.angle
		

#Servo Objects		
shoulderServo = robotServo(pin = 0, angle = 20)
elbowServo = robotServo(pin = 1, angle = 40)
wristServo = robotServo(pin = 2, angle = 90)
clawServo = robotServo(pin = 3, angle = 103, minAngle = 103)
camServo = robotServo(pin = 4, angle = 90, minAngle = 55, maxAngle = 95)
	
def initPosition():
	shoulderServo.angle = shoulderAngle
	shoulderServo.setServoAngle()
	elbowServo.angle = elbowAngle
	elbowServo.setServoAngle()
	wristServo.angle = wristAngle
	wristServo.setServoAngle()
	clawServo.angle = clawAngle
	clawServo.setServoAngle()
	camServo.angle = camAngle
	camServo.setServoAngle()

if __name__ == '__main__': #Test Code
	
	initPosition()

	for i in range(180): #The cam servo trys to turn from 0 to 180 degrees (should only move from 55 to 95).
		camServo.angle = i
		camServo.setServoAngle()
		print (camServo.angle) #Check angle value
		sleep(0.01)
	
