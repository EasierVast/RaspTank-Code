
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
import cv2
from time import sleep
import Robot_Move as move
import Robot_Camera as cam
from Robot_Camera import fps, prevTime, dispW, dispH

speed = 0.5 #1 = full speed
currentDirection = "STOP"

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
		if cv2.waitKey(1) == ord('q'): #if detect 'q' press
			break
		#direction = input("Input direction:")
		#robotMove(direction)
		objX, objY, objWidth, objHeight = cam.getOOI(img)
		img = cam.drawBoundingBox(img, objX, objY, objWidth, objHeight)
		#fps, prevTime, img = cam.showFPS(fps, prevTime, img)
		cv2.imshow("Camera Feed", img)
		
		dispCenterX = dispW/2
		objCenterX = objWidth/2
		panError = (objX + objCenterX) - dispCenterX
		#print("panError = " + str(panError))
		if panError > 50:
			if currentDirection != "RIGHT":
				print("RIGHT")
				currentDirection = "RIGHT"
		elif panError < -50:
			if currentDirection != "LEFT":
				print("LEFT")
				currentDirection = "LEFT"
		else:
			if currentDirection != "STOP":
				print("STOP")
				currentDirection = "STOP"
		 
except KeyboardInterrupt: #ctrl+C to stop code
    print("EXIT LOOP")
    move.stopTurn() #make sure motor is off

