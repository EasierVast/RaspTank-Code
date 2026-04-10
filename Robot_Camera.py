
import cv2
from picamera2 import Picamera2
import time

fps = 0
prevTime = 0
dispW = 640
dispH = 360

def initCam():
    #Initialise Camera
    robotCam = Picamera2()
    robotCam.preview_configuration.main.size = (dispW, dispH)
    robotCam.preview_configuration.main.format = "RGB888" #so I don't need to convert the format later for display purposes
    robotCam.preview_configuration.controls.FrameRate = 30 #desired framerate, may not be actual framerate
    robotCam.start()
    return robotCam

def calcFPS(fps, prevTime):
    currTime = time.time()
    timeDiff = currTime - prevTime 
    fps = .9*fps + .1*(1/timeDiff) #using low pass filter for cleaner data value
    prevTime = currTime
    return fps, prevTime

def showFPS(fps, prevTime, img):
    pos = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    height = 1
    color = (0, 255, 0) #GREEN, default colour for fps counters
    weight = 3
    
    fps, prevTime = calcFPS(fps, prevTime)
    cv2.putText(img, str(int(fps)), pos, font, height, color, weight)
    return fps, prevTime, img
    #print(int(fps)) #make it 'int' to round the number
    
def drawBox(img):
    upperLeft = (250, 100) #placeholder for testing
    lowerRight = (400, 200) #placeholder for testing
    color = (0, 0, 255) #RED
    weight = 3
    cv2.rectangle(img, upperLeft, lowerRight, color, weight)
    return img

#Display camera feed
robotCam = initCam()
while True:
    img = robotCam.capture_array()
    fps, prevTime, img = showFPS(fps, prevTime, img)
    img = drawBox(img)
    cv2.imshow("Camera Feed", img)
    if cv2.waitKey(1) == ord('q'): #if detect 'q' press
        break
    
cv2.destroyAllWindows()
