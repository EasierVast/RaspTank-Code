
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
import cv2
from time import sleep
import Robot_Move as move
import Robot_Camera as cam

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
	robotCam = cam.initCam()
	while True:
		img = robotCam.capture_array()
		cv2.imshow("Camera Feed", img)
		if cv2.waitKey(1) == ord('q'): #if detect 'q' press
			break
		#direction = input("Input direction:")
		#robotMove(direction)
except KeyboardInterrupt: #ctrl+C to stop code
    print("EXIT LOOP")
    move.stopTurn() #make sure motor is off

