
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
direction = "STOP"
currentDirection = "STOP"
mode = "STANDBY"
	
def calcPanError(dispW, objWidth, objX):
	dispCenterX = dispW/2
	objCenterX = objWidth/2
	panError = (objX + objCenterX) - dispCenterX
	return panError

try:
	robotCam = cam.initCam()
	while True:
		img = robotCam.capture_array()
		if cv2.waitKey(1) == ord('s') and mode != "STANDBY":
			print("Robot in Standby Mode")
			mode = "STANDBY"
		if cv2.waitKey(1) == ord('m') and mode != "MOVE":
			mode = "MOVE"
			print("Robot in Move Mode")
		if cv2.waitKey(1) == ord('q'): #if detect 'q' press
			move.stopTurn() #make sure motor is off
			break
			
		objX, objY, objWidth, objHeight = cam.getOOI(img)
		img = cam.drawBoundingBox(img, objX, objY, objWidth, objHeight)
		#fps, prevTime, img = cam.showFPS(fps, prevTime, img)
		cv2.imshow("Camera Feed", img)
		
		if mode == "MOVE":
			panError = calcPanError(dispW, objWidth, objX)
			#print("panError = " + str(panError))
			if panError > 100:
				if currentDirection != "RIGHT":
					print("RIGHT")
					direction = "RIGHT"
					currentDirection = "RIGHT"
			elif panError < -100:
				if currentDirection != "LEFT":
					print("LEFT")
					direction = "LEFT"
					currentDirection = "LEFT"
			else:
				if currentDirection != "STOP":
					print("STOP")
					direction = "STOP"
					currentDirection = "STOP"
			move.robotMove(direction, speed)
		 
except KeyboardInterrupt: #ctrl+C to stop code
    print("EXIT LOOP")
    move.stopTurn() #make sure motor is off

