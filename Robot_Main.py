
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from time import sleep
import Robot_Move as move

speed = 0.5 #1 = full speed

#Move the robot    
def robotMove(direction):
    if direction.upper() == "LEFT":
        print("Left")
        move.leftTurn(speed)
    elif direction.upper() == "RIGHT":
        print("Right")
        move.rightTurn(speed)
    elif direction.upper() == "STOP":
        move.stopTurn()
    else:
        print("Invalid Input")

try:
    while True:
        direction = input("Input direction:")
        robotMove(direction)
except KeyboardInterrupt: #ctrl+C to stop code
    print("EXIT LOOP")
    stopTurn() #make sure motor is off

