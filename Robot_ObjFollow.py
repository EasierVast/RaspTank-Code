
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
import cv2
from time import sleep
import Robot_Move as move
import Robot_Camera as cam
from Robot_Camera import objExist, fps, prevTime, dispW, dispH
import Robot_Servo as servo
from Robot_Servo import camServo

speed = 0.25 #1 = full speed
panDirection = "STOP"
currentPanDirection = "STOP"
tiltDirection = "STOP"
currentTiltDirection = "STOP"
mode = "WAIT"
panErrorRange = 30
tiltErrorRange = 30
	
def calcError(disp, objMeasure, objAxis):
	dispCenter = disp/2
	objCenter = objMeasure/2
	error = (objAxis + objCenter) - dispCenter
	return error
	
def initDefaultState():
	move.stopTurn() #make sure motor is off
	servo.initPosition() #move servos to initial positions

try:
	robotCam = cam.initCam()
	initDefaultState()
	
	while True:
		img = robotCam.capture_array()
		if cv2.waitKey(1) == ord('w') and mode != "WAIT":
			print("Robot in Wait Mode")
			mode = "WAIT"
		if cv2.waitKey(1) == ord('m') and mode != "MOVE":
			mode = "MOVE"
			print("Robot in Move Mode")
		if cv2.waitKey(1) == ord ('s'):
			objExist = cam.getObjectOfInterest(robotCam)
		if cv2.waitKey(1) == ord('q'): #if detect 'q' press
			initDefaultState()
			break
			
		objX, objY, objWidth, objHeight = cam.getOOI(img, objExist)
		img = cam.drawBoundingBox(img, objX, objY, objWidth, objHeight)
		#fps, prevTime, img = cam.showFPS(fps, prevTime, img)
		cv2.imshow("Camera Feed", img)
		
		if mode == "WAIT":
			initDefaultState()
		
		if mode == "MOVE":
			panError = calcError(dispW, objWidth, objX)
			#print("panError = " + str(panError))
			tiltError = calcError(dispH, objHeight, objY)
			#print("tiltError = " + str(tiltError))
			
			if panError > panErrorRange:
				if currentPanDirection != "RIGHT":
					#print("RIGHT")
					panDirection = "RIGHT"
					currentPanDirection = "RIGHT"
			elif panError < -panErrorRange:
				if currentPanDirection != "LEFT":
					#print("LEFT")
					panDirection = "LEFT"
					currentPanDirection = "LEFT"
			else:
				if currentPanDirection != "STOP":
					#print("STOP PAN")
					panDirection = "STOP"
					currentPanDirection = "STOP"
			move.robotMove(panDirection, speed)
			
			if tiltError > tiltErrorRange:
				camServo.angle = camServo.angle + 1
				if currentTiltDirection != "DOWN":
					#print("DOWN")
					currentTiltDirection = "DOWN"
			elif tiltError < -tiltErrorRange:
				camServo.angle = camServo.angle - 1
				if currentTiltDirection != "UP":
					#print("UP")
					currentTiltDirection = "UP"
			else:
				if currentTiltDirection != "STOP":
					#print("STOP TILT")
					currentTiltDirection = "STOP"
			camServo.setServoAngle()
	
		 
except KeyboardInterrupt: #ctrl+C to stop code
    print("EXIT LOOP")
    initDefaultState()

