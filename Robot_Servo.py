
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

"""
#Servo Pins
shoulderPin = 0
elbowPin = 1
wristPin = 2
clawPin = 3 #closed claw at 100 (103 for safety)
camPin = 4 #movement range 50 - 100

#Servo Default Positions
shoulderAngle = 20
elbowAngle = 40
wristAngle = 90
clawAngle = 103
camAngle = 90
"""

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
		servoAngle.angle = self.angle

#Servo Objects		
shoulder = robotServo(pin = 0, angle = 20)
elbow = robotServo(pin = 1, angle = 40)
wrist = robotServo(pin = 2, angle = 90)
claw = robotServo(pin = 3, angle = 103, minAngle = 103)
cam = robotServo(pin = 4, angle = 90, minAngle = 10, maxAngle = 100)
	
def initPosition():
	shoulder.setServoAngle()
	elbow.setServoAngle()
	wrist.setServoAngle()
	claw.setServoAngle()
	cam.setServoAngle()

if __name__ == '__main__': #Test Code
	
	initPosition()
	
