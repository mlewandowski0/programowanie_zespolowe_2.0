import keyboard
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
Motor1A = 16
Motor1B = 18
Motor1E = 22
Motor2A = 19
Motor2B = 21
Motor2E = 23

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)


while True:
    try:
        if keyboard.is_pressed( 'w'):
            print('w')
        elif keyboard.is_pressed( 's'):
            print('cf') 

        elif keyboard.is_pressed( 'a'):
            print('a')
            

        elif keyboard.is_pressed( 'd'):
            print('d')


    except:
        GPIO.cleanup()
GPIO.cleanup()

import pygame, sys
import pygame.locals

pygame.init()
BLACK = (0,0,0)
WIDTH = 1280
HEIGHT = 1024

windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
windowSurface.fill(BLACK)

while True:
        for event in pygame.event.get():
            if event.key == pygame.K_w:
                print('w')
                GPIO.output(Motor1A, GPIO.HIGH)
                GPIO.output(Motor1B, GPIO.LOW)
                GPIO.output(Motor1E, GPIO.HIGH)
                GPIO.output(Motor2A, GPIO.HIGH)
                GPIO.output(Motor2B, GPIO.LOW)
                GPIO.output(Motor2E, GPIO.HIGH)
                #Do what you want to here
            if event.key == pygame.K_s:
               pass
            if event.key == pygame.K_a:
                print('a')
                GPIO.output(Motor1A, GPIO.HIGH)
                GPIO.output(Motor1B, GPIO.LOW)
                GPIO.output(Motor1E, GPIO.HIGH)
                GPIO.output(Motor2E, GPIO.LOW)
            
            if event.key == pygame.K_d:
                print('d')
                GPIO.output(Motor2A, GPIO.HIGH)
                GPIO.output(Motor2B, GPIO.LOW)
                GPIO.output(Motor2E, GPIO.HIGH)
                GPIO.output(Motor1E, GPIO.LOW) 


            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

