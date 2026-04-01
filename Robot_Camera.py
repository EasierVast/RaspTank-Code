
import cv2
from picamera2 import Picamera2

#Initialise Camera
robotCam = Picamera2()
robotCam.preview_configuration.main.size = (720, 480) #set image resolution
robotCam.preview_configuration.main.format = "RGB888" #set colour format ?BGR?
robotCam.preview_configuration.controls.FrameRate = 30 #set desired framerate
robotCam.start() #start camera

while True:
    frame = robotCam.capture_array() #get frame
    cv2.imshow("Camera Feed", frame) #show frame
    if cv2.waitKey(1) == ord('q'): #if detect 'q' press
        break
cv2.destroyAllWindows()
