#!/usr/bin/python3

from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
from random import randint
import thread

i = 0 
add = 30 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)
servo1 = GPIO.PWM(3, 50)
servo1.start(0)
servo2 = GPIO.PWM(5, 50)
servo2.start(0)

def setAngle(servo, angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    servo.ChangeDutyCycle(duty)
    sleep(0.25)
    GPIO.output(3, False)
    servo.ChangeDutyCycle(0)

def servos():
    global i, add 
    while True:
        if i > 180:
            add *= -1
        elif i < 0:
            add *= -1
        
        setAngle(servo1, randint(0,180))
        sleep(0.5)


thread.start_new_thread(servos, ())

camera = PiCamera()
camera.preview_fullscreen = False
camera.preview_window=(100, 100, 1000, 800)
camera.start_preview()
effects = [u'sketch', u'posterise', u'gpen', u'film', u'pastel',  u'emboss', u'negative', u'colorswap', u'colorpoint',u'hatch', u'watercolor', u'cartoon', u'washedout', u'solarize', u'oilpaint']

while True:
    for effect in effects:
        camera.image_effect = effect
        camera.annotate_text = 'Effect: %s' % effect
        sleep(5)
    
camera.stop_preview()
servo1.stop()
servo2.stop()
GPIO.cleanup()
