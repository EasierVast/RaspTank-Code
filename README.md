In this project, I am hoping to further my understanding of how to utilise a Raspberry Pi within a robot. For this project, I wanted to have my robot track and follow an object as it moves within the view of the robot's camera. Initially I did not know how I was going to define the object of interest, as I wanted to give later users the ability to set their own object of interest. I decided to implement a system where the robot has a standby mode and a move mode, where during the standby mode the user can have the robot take a picture of what it sees, then get a definition of the object of interest from the image.

## Technologies
- OpenCV
- Numpy
- Board
- Busio
- Adafruit PCA9685
- Adafruit Motor

## Features
- Defines its own object of interest by taking a screenshot and extracting an effective colour range from the screenshot.
- Can track/follow the Object of Interest on the x-axis by moving the entire robot.

## Installation
For this project, the hardware that was used was the Adeept RaspTank Metal V1; a V2 version of this robot has been released, but this code has not been tested on the newer hardware.
- Build the robot and install the Raspberry Pi OS as instructed in the tutorial included with the robot; this project does not use any other dependencies other than the ones that have been installed during the tutorials.
- Clone this repository to your Raspberry Pi.

## Running the Program
- Within the repository, execute and run the script 'Robot_Main.py'.
- Position/Hold the object of interest in front of the robot's camera, so that the object is in the centre of the camera feed.
- Press the 's' key on your keyboard to have the robot take a screenshot; the command line will confirm if a screenshot is taken.
- Once a screenshot has been taken, press the 'm' key on your keyboard to set the robot in motion; the robot should now follow your object of interest as you move it around.
- To return the robot to its wait state, press the 'w' key on your keyboard.
- To stop the program press the 'q' key on your keyboard.

Thank you Adeept for your robotic hardware and your tutorials, which have aided in my journey on implementing Raspberry Pi into my projects.
https://www.adeept.com/
