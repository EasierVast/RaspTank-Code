
import cv2
from picamera2 import Picamera2
import time

fps = 0
dispW = 640
dispH = 360
pos = (10, 30)
font = cv2.FONT_HERSHEY_SIMPLEX
height = 1
fpsColor = (0, 255, 0) #GREEN, default colour for fps counters
weight = 3


#Initialise Camera
robotCam = Picamera2()
robotCam.preview_configuration.main.size = (dispW, dispH)
robotCam.preview_configuration.main.format = "RGB888" #so I don't need to convert the format later for display purposes
robotCam.preview_configuration.controls.FrameRate = 30 #desired framerate, may not be actual framerate
robotCam.start() 

def calcFPS(fps, tStart):
    tEnd = time.time()
    loopTime = tEnd - tStart 
    fps = .9*fps + .1*(1/loopTime) #using low pass filter for cleaner data value
    return fps
    #print(int(fps)) #make it 'int' to round the number

#Display camera feed
while True:
    tStart = time.time()
    img = robotCam.capture_array()
    if fps != 0:
        cv2.putText(img, str(int(fps)), pos, font, height, fpsColor, weight)
    cv2.imshow("Camera Feed", img)
    if cv2.waitKey(1) == ord('q'): #if detect 'q' press
        break
    fps = calcFPS(fps, tStart)
    
cv2.destroyAllWindows()
