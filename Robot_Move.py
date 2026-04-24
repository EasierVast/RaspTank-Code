
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from time import sleep

MOTOR_1_IN1 =  15      #Define the positive pole of left motor
MOTOR_1_IN2 =  14      #Define the negative pole of left motor
MOTOR_2_IN1 =  12      #Define the positive pole of right motor
MOTOR_2_IN2 =  13      #Define the negative pole of right motor

PWM = 60 #PWM frequency to 60hz (standard value)

#Initialize I2C bus using busio
i2c = busio.I2C(SCL, SDA)

#Create a simple PCA9685 class instance for the Motor Driver
pwm_motor = PCA9685(i2c, address=0x5f) #default 0x40 but HAT uses 0x5f
pwm_motor.frequency = PWM #Set PWM Frequency

#Define the Motors (motor1 = left motor, motor2 = right motor)
motor1 = motor.DCMotor(pwm_motor.channels[MOTOR_1_IN1],pwm_motor.channels[MOTOR_1_IN2] )
motor2 = motor.DCMotor(pwm_motor.channels[MOTOR_2_IN1],pwm_motor.channels[MOTOR_2_IN2] )

#Turn robot left until another command received
def leftTurn(speed):
    motor1.throttle = -speed
    motor2.throttle = speed

#Turn robot right until another command received    
def rightTurn(speed):
    motor1.throttle = speed
    motor2.throttle = -speed
    
#Stop robot movement, no coasting
def stopTurn():
    motor1.throttle = 0.0
    motor2.throttle = 0.0
    
#Move the robot    
def robotMove(direction, speed):
    if direction.upper() == "LEFT":
        #print("Left")
        leftTurn(speed)
    elif direction.upper() == "RIGHT":
        #print("Right")
        rightTurn(speed)
    elif direction.upper() == "STOP":
        stopTurn()
    else:
        print("Invalid Input")


if __name__ == '__main__': #Test Code
    
    speed = 0.5 #1 = full speed

    try:
        while True:
            direction = input("Input direction:")
            robotMove(direction, speed)
    except KeyboardInterrupt: #ctrl+C to stop code
        print("EXIT LOOP")
        stopTurn() #make sure motor is off

