
import cv2
from picamera2 import Picamera2
import time
import numpy as np

fps = 0
prevTime = 0
dispW = 640
dispH = 360

try:
    file = open('ObjectOfInterest.jpg')
except:
    objExist = False
else:
    objExist = True

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
    
def getObjectOfInterest(robotCam):
    robotCam.capture_file("ObjectOfInterest.jpg")
    print("Screenshot Taken")
    objExist = True
    return objExist
    
def getObjectColor(dispW, dispH, filepath):
    image = cv2.imread(filepath)
    centerRow = int(dispH/2)
    centerColumn = int(dispW/2)
    objectColor = image[centerRow, centerColumn]
    return objectColor
    
def createMask(img, color):
    numpyColor = np.uint8([[color]]) #make colour value into 3D numpy array
    hsvNumpyColor = cv2.cvtColor(numpyColor, cv2.COLOR_BGR2HSV)
    lowerLimit = hsvNumpyColor[0][0][0] - 10, 100, 100
    upperLimit = hsvNumpyColor[0][0][0] + 10, 255, 255
    
    #turn the limit tuples into numpy arrays
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)
    
    #prepare video to generate mask
    hsvImg  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)
    return mask
    
def getContour(img, mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = sorted(contours, key = lambda x:cv2.contourArea(x), reverse = True)
    cv2.drawContours(img, contour, 0, (0,255,0), 3)
    return img

def drawBox(img):
    upperLeft = (250, 100) #placeholder for testing
    lowerRight = (400, 200) #placeholder for testing
    color = (0, 0, 255) #RED
    weight = 3
    cv2.rectangle(img, upperLeft, lowerRight, color, weight)
    return img
    
def showImage(filePath):
    image = cv2.imread(filePath)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyWindow("Image")

if __name__ == '__main__': #Test Code
    
    #Display camera feed
    robotCam = initCam()
    while True:
        img = robotCam.capture_array()
        if cv2.waitKey(1) == ord('q'): #if detect 'q' press
            break
        elif cv2.waitKey(1) == ord('s'):
            objExist = getObjectOfInterest(robotCam)
        elif cv2.waitKey(1) == ord('p') and objExist == True:
            showImage('ObjectOfInterest.jpg')
           
        if objExist == True:
            objectColor = getObjectColor(dispW, dispH, 'ObjectOfInterest.jpg')
            mask = createMask(img, objectColor)
            cv2.imshow("Mask Check", mask)
            img = getContour(img, mask)
        #img = drawBox(img)
        #fps, prevTime, img = showFPS(fps, prevTime, img)
        cv2.imshow("Camera Feed", img)  
    
cv2.destroyAllWindows()
