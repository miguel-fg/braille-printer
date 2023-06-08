# Raspberry Pi powered braille printer prototype
This project aims to create a Braille printer using a Raspberry Pi, a camera, OpenCV, and Tesseract. The printer captures a snapshot of text, extracts the characters using optical character recognition (OCR), and translates each character into movement instructions for three motors. These motors generate a strip of paper with corresponding Braille tactile bumps.

## Demo
https://github.com/miguel-fg/braille-printer/assets/72409412/a946d35b-01bf-476c-819b-db31384224c9


## Requirements
To run this project, you will need the following:
 - Raspberry Pi 4 with Raspbian OS installed
 - Raspberry Pi Camera module
 - Python 3.x
 - OpenCV library
 - Tesseract OCR library
 - 3D printed STL files in PLA with at least 50% infill
 - 1 sg90 DC servomotor
 - 1 mg995 DC servomotor
 - 1 130 size DC hobby motor
 - 1 L298n H bridge motor driver

## An explanation of the braille system
The tactile writing system characters are formed using a combination of six raised dots in a 3 x 2 matrix. The number and arrangement of the dots distinguishes a character from another. 
  ⠠⠓⠑⠇⠇⠕ ⠺⠕⠗⠇⠙ (Hello world)

### The role of the motors
1. The DC motor's task is simple, it drags the strip of paper a predefined amount of distance along the printer's bed. This motion allows the bumps to move in the horizontal axis of the matrix.
2. The smaller sg90 servomotor moves a needle to 1 of 3 possible positions, allowing the printing of 3 bumps along the matrix's vertical axis.
3. The heavier mg995 servomotor moves the smaller servomotor up and down between needle position shifts, perforating the piece of paper and printing a bump on the opposite side.

## Physical assembly
The base of the prototype is the case of the Raspberry Pi connected to the perforation bed. 
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/26d7047a-d48b-4d8e-b5c4-9b0e11c7359d)

The housing system for both servomotors is then fitted into place.
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/f2a93450-5f4b-4624-b94a-bacb70076343)

With the final piece, the small hub for the DC motor fitted at the front of the perforation bed.
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/637b717c-cfe8-4e0b-88b3-5ca490e06660)

The final assembly should look like this
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/9dd0a2f5-bada-4d82-8760-9073b725c7bb)
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/74c50718-df81-48d4-851e-b19d50c1b468)


### Electric schematic
The final step is to ensure all the connections are made as follows:
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/7c8d2f09-c17d-4068-9c61-dca79622dec0)
![image](https://github.com/miguel-fg/braille-printer/assets/72409412/5795d02e-cf38-419e-92ea-bb057eb72001)

## Usage
1. Ensure that the camera module and strip of paper are correctly attached to the Raspberry Pi
2. Point the camera at text and run the following command to start the printer
  ```
  python FullT_dc.py
  ```
3. The printer will capture an image, filter it, generate an array of strings, and generate the corresponding PWM signals to move the motors.
4. The strip of paper can then be removed from the DC motor and inspected to see the results.


