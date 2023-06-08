#!usr/bin/env python
# -*- coding: utf-8 -*-
from cv2 import *
import pytesseract
import numpy as np
import RPi.GPIO as GPIO
import sys
from time import sleep
import pigpio

# uncomment to read image from camera

#cam = VideoCapture(0)   # 0 -> index of camera
#s, img1 = cam.read()
#if s:    # frame captured without any errors
    #img1=cv2.rotate(img1, cv2.ROTATE_90_CLOCKWISE)
   # namedWindow("cam-test")
  #  imshow("cam-test",img1)
 #   destroyWindow("cam-test")
#    imwrite("1.TIFF",img1) #save image


# or load an image directly via openCV
img = cv2.imread("elliottC.TIFF")



# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

def split(word): 
    return [char for char in word]

def SetAngle(angle):
    duty = angle / 18 + 2
    #GPIO.output(3, True)
    duty = duty/100
    pi.hardware_PWM(13, 50, int(1e6*duty))
    #pwm.ChangeDutyCycle(duty)
    sleep(1)
    #GPIO.output(3, False)
    pi.hardware_PWM(13, 50, 0)
    
def SetAngle2(angle):
    duty = angle / 18 + 2
    duty = duty/100
    pi.hardware_PWM(12, 50, int(1e6*duty))
    #GPIO.output(5, True)
    #pwm2.ChangeDutyCycle(duty)
    sleep(1)
    #GPIO.output(5, False)
    #pwm2.ChangeDutyCycle(0)
    pi.hardware_PWM(12, 50, 0)

def Pr():
    #try:
        SetAngle2(iz)
        sleep(2)
        SetAngle(abajo)
        sleep(2)
        SetAngle(arriba)
        sleep(2)
    #except KeyboardInterrupt:
     #   pwm.stop()
      #  pwm2.stop()
       # pwm_dc.stop()
        #GPIO.cleanup()
        #sys.exit(0)
    
def Mid():
    #try:
        SetAngle2(centro)
        sleep(2)
        SetAngle(abajo)
        sleep(2)
        SetAngle(arriba)
        sleep(2)
   # except KeyboardInterrupt:
   #     pwm.stop()
   #     pwm_dc.stop()
   #     pwm2.stop()
   #     GPIO.cleanup()
   #     sys.exit(0)
    
def last():
    #try:
        SetAngle2(der)
        sleep(2)
        SetAngle(abajo)
        sleep(2)
        SetAngle(arriba)
        sleep(2)
    #except KeyboardInterrupt:
    #    pwm.stop()
    #    pwm_dc.stop()
    #    pwm2.stop()
    #    GPIO.cleanup()
    #    sys.exit(0)
        
def step():    
    #try:
        pwm_dc.ChangeDutyCycle(20) 
        sleep(0.5)
        pwm_dc.ChangeDutyCycle(0)
        sleep(2)
    #except KeyboardInterrupt:
     #       pwm.stop()
      #      pwm_dc.stop()
       #     pwm2.stop()
        #    GPIO.cleanup()
         #   sys.exiy(0)
        


gray = get_grayscale(img)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

# extract text from image
custom_config = r'--oem 3 --psm 6'
sret=pytesseract.image_to_string(canny, lang='spa', config=custom_config)
#sret2=pytesseract.image_to_string(gray, lang='spa', config=custom_config)
#sret3=pytesseract.image_to_string(opening, lang='spa', config=custom_config)
print(sret)
abc= ["a"]
#cv2.imshow('opening', opening)
# print extracted text
lista=split(sret)
x=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)
#GPIO.setup(5, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#pwm = GPIO.PWM(3, 50)
#pwm2 = GPIO.PWM(5, 50)
pwm_dc = GPIO.PWM(11, 100)
pwm_dc.start(0)
GPIO.output(13,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
pi = pigpio.pi()
pi.hardware_PWM(12, 50,0)
pi.hardware_PWM(13, 50,0)
#pwm.start(0)
#pwm2.start(0)
arriba=130
abajo=85
der=70
centro=80
iz=90



SetAngle(arriba)
sleep(2)
SetAngle2(centro)
sleep(2)

for count in lista:
    if (ord(lista[x])==32 or ord(lista[x])==13):
        #space
        print(lista[x])
    elif (ord(lista[x])==65 or ord(lista[x])==97):
        #A
        Pr()
        step()
        step()
        print(lista[x])
    elif (ord(lista[x])==66 or ord(lista[x])==98):
        #B
        Pr()
        Mid()
        step()
        step()
        print(lista[x])
    elif (ord(lista[x])==67 or ord(lista[x])==99):
        #C o c
        Pr()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==68 or ord(lista[x])==100):
        #D o d
        Pr()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==69 or ord(lista[x])==101):
        #E o e
        Pr()
        step()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==70 or ord(lista[x])==102):
        #F o f
        Pr()
        Mid()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==71 or ord(lista[x])==103):
        #G o g
        Pr()
        Mid()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==72 or ord(lista[x])==104):
        #H o h
        Pr()
        Mid()
        step()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==73 or ord(lista[x])==105):
        #I o i
        Mid()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==74 or ord(lista[x])==106):
        #J o j
        Mid()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==75 or ord(lista[x])==107):
        #K o k
        Pr()
        last()
        step()
        step()
        print(lista[x])
    elif (ord(lista[x])==76 or ord(lista[x])==108):
        #L o l
        Pr()
        Mid()
        last()
        step()
        step()
        print(lista[x])
    elif (ord(lista[x])==77 or ord(lista[x])==109):
        #M o m
        Pr()
        last()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==78 or ord(lista[x])==110):
        #N o n
        Pr()
        last()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==79 or ord(lista[x])==111):
        #O o o
        Pr()
        last()
        step()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==80 or ord(lista[x])==112):
        #P o p
        Pr()
        Mid()
        last()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==81 or ord(lista[x])==113):
        #Q o q
        Pr()
        Mid()
        last()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==82 or ord(lista[x])==114):
        #R o r
        Pr()
        Mid()
        last()
        step()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==83 or ord(lista[x])==115):
        #S o s
        Mid()
        last()
        step()
        Pr()
        step()
        print(lista[x])
    elif (ord(lista[x])==84 or ord(lista[x])==116):
        #T o t
        Mid()
        last()
        step()
        Pr()
        Mid()
        step()
        print(lista[x])
    elif (ord(lista[x])==85 or ord(lista[x])==117):
        #U o u
        Pr()
        last()
        step()
        last()
        step()
        print(lista[x])
    elif (ord(lista[x])==86 or ord(lista[x])==118):
        #V o v
        Pr()
        Mid()
        last()
        step()
        last()
        step()
        print(lista[x])
    elif (ord(lista[x])==87 or ord(lista[x])==119):
        #W o w
        Mid()
        step()
        Pr()
        Mid()
        last()
        step()
        print(lista[x])
    elif (ord(lista[x])==88 or ord(lista[x])==120):
        #X o x
        Pr()
        last()
        step()
        Pr()
        last()
        step()
        print(lista[x])
    elif (ord(lista[x])==89 or ord(lista[x])==121):
        #Y o y
        Pr()
        last()
        step()
        Pr()
        Mid()
        last()
        step()
        print(lista[x])
    elif (ord(lista[x])==90 or ord(lista[x])==122):
        #Z o z
        Pr()
        last()
        step()
        Mid()
        last()
        step()
        print(lista[x])
    else:
        print(lista[x])
    x+=1
   
