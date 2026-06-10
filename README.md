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
- Can track/follow the object of interest along both the x-axis (by moving the entire robot) and y-axis (via a servo in the camera).

## Installation
### Hardware Requirements:
- **Tested on:** Adeept RaspTank Metal V1 *(V2 compatibility untested)*

### Setup Instructions:
1. **Robot Assembly**:  
   Follow the tutorials included with your Adeept RaspTank Metal to:
   - Assemble the RaspTank hardware  
   - Install Raspberry Pi OS  

2. **Dependencies**:  
   No additional dependencies required beyond those installed during the tutorial process.

3. **Clone Repository**:  
   ```bash
   git clone https://github.com/EasierVast/RaspTank-Code.git
   ```
## Running Object Follow Program
1. Within the repository, execute the script:
   ```bash
   python Robot_ObjFollow.py
   ```

2. Initialize target object:
   - Position object in center of camera view
   - Press `s` to capture reference screenshot
     
   **Note:** Only required once unless changing the object of interest.

## Operation Modes
| Mode | Description |
|------|-------------|
| WAIT | Robot stationary, camera at default angle |
| MOVE | Robot actively follows target object |

**Note:** When starting the program the robot will be in WAIT mode.*

## Key Commands
| Key | Action |
|-----|--------|
| `s` | Capture screenshot |
| `m` | Switch to MOVE mode |
| `w` | Switch to WAIT mode |
| `q` | Quit program |

**Note:** Confirmation of each command will appear in terminal.

The robot will continuously track the object while in MOVE mode. Use `w` to pause tracking or `q` to exit completely.
  
### Video Demonstrations

https://github.com/user-attachments/assets/ede39aba-feab-4a02-9fab-08957aded318

https://github.com/user-attachments/assets/b069f2fc-189b-4038-8cd3-eb7370d0717f

Thank you Adeept for your robotic hardware and your tutorials, which have aided in my journey on implementing Raspberry Pi into my projects.
https://www.adeept.com/
