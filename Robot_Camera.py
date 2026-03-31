
import cv2
from picamera2 import Picamera2

#Initilise Camera
robotCam = Picamera2()
robotCam.preview_configuration.main.size = (720, 480) #set image resolution
robotCam.preview_configuration.main.format = "RGB888" #set colour format ?BGR?
robotCam.configure("preview")

robotCam.start()
while True:
    frame = robotCam.capture_array()
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
