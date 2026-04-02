
import cv2
from picamera2 import Picamera2
import time

fps = 0

#Initialise Camera
robotCam = Picamera2()
robotCam.preview_configuration.main.size = (720, 480) #set image resolution
robotCam.preview_configuration.main.format = "RGB888" #set colour format ?BGR?
robotCam.preview_configuration.controls.FrameRate = 30 #set desired framerate
robotCam.start() #start camera

while True:
    tStart = time.time()
    frame = robotCam.capture_array() 
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) == ord('q'): #if detect 'q' press
        break
    tEnd = time.time()
    loopTime = tEnd - tStart #time for iteration of loop (time at end - time at start)
    fps = .9*fps + .1*(1/loopTime) #using low pass filter for cleaner data value
    print(int(fps)) #make it 'int' to round the number
cv2.destroyAllWindows()
