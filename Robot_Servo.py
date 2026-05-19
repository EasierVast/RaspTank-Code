
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
from time import sleep

shoulderPin = 0
elbowPin = 1
wristPin = 2
clawPin = 3 #closed claw at 0
camPin = 4 #movement range 50 - 100

PWM = 50 #PWM frequency to 50hz (standard value for servo)

#Initialize I2C bus using busio
i2c = busio.I2C(SCL, SDA)

#Create a simple PCA9685 class instance for the Servo Driver
pca = PCA9685(i2c, address=0x5f) #default 0x40 but HAT uses 0x5f
pca.frequency = PWM

#Intialize servo & set angle
servoShoulder = servo.Servo(pca.channels[shoulderPin], min_pulse=200, max_pulse=2400, actuation_range=180)
servoShoulder.angle = 90
