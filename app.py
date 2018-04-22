#!/usr/bin/python3
import sys
import threading
import time
import random
import argparse
import subprocess
import gevent
import psutil

from importlib import import_module
from flask import Flask, render_template, Response
from flask_socketio import SocketIO, send, emit
from constants import *
 

# Raspberry Pi camera module (requires picamera package)
couldStream = True
try:
    from camera_pi import Camera
except ImportError:
    print(WARNING_PREFIX + " didn't find module picamera so streaming from raspberry isn't available !")
    couldStream = False

# Raspberry Pi electronics 
electronicsEnabled = True
try:
    import RPi.GPIO as GPIO
except ImportError:
    electronicsEnabled = False
    print(WARNING_PREFIX + " didn't import raspberry pi electronics module !")

# create flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'l1v3-f0r-l0lz'
socketio = SocketIO(app)

# constants for breaking other 'daemon' threads
isServingFiles = True
verboseMode    = False
args           = None
featuresStates = {"flashlight": False, "laser":False, "buzzing":False}
socketConn     = False

################################################################################
# IMAGE PROCESSING ON SERVER SIDE
def changeCameraConfig(effect_name):
    if args.verbose is not None:
        print(GREEN_ESCAPE + " changing to " + effect_name)

def processFrame(frame):
    pass

################################################################################
# ELECTRONIC LOGIC
servo1, servo2 = None, None
servo1Pin, servo2Pin = 3, 5
frequency      = 50
Motor1A, Motor1B, Motor1E = 16, 18, 22
Motor2A, Motor2B, Motor2E = 19, 21, 23


def electronicSetup():
    global servo1, servo2
    GPIO.setmode(GPIO.BOARD)

    # setup pins 
    GPIO.setup(servo1Pin, GPIO.OUT)
    GPIO.setup(servo2Pin, GPIO.OUT)
    
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    
    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)
    
    # setup servos
    servo1 = GPIO.PWM(3, frequency)
    servo1.start(0)
    servo2 = GPIO.PWM(5, frequency)
    servo2.start(0)

# set angle of servomechanism
def setAngle(servo, pin, angle):
    duty = angle / 18 + 2
    GPIO.output(pin, True)
    servo.ChangeDutyCycle(duty)
    GPIO.output(pin, False)
    servo.ChangeDutyCycle(0)

def cleanup():
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()

################################################################################
# ROUTING
@app.route('/')
def robot_controls():
    """Video streaming home page."""
    if not couldStream and verboseMode:
        print(RED_ESCAPE + u" CAN'T STREAM ! MONKEY ALERT " + ESCAPE_END)
    return render_template('robot_controls.html',streamState=couldStream)
    

@app.route('/video_feed')
def video_feed():
        if couldStream:
            """Video streaming route."""
            return Response(genStream(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

################################################################################    
# STREAMING
def genStream(camera):
    """Video streaming generator function."""
    while True:
        socketio.emit('data', {"xd":'xd'})
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

################################################################################    
# WEB SOCKET LOGIC AND THREADING

@socketio.on('debug-send')
def handleMyEvent(e):
    try:
        print("debug-send received; msg : " + str(e))
    except TypeError:
        print("TypeError in received debug-send")

@socketio.on("connected")
def handleStartingConnection():
    global socketConn
    print(GOOD_PREFIX + " starting web socket connection !")
    socketConn = True
    emit("data", generateData())

@socketio.on("request")
def handleReturningRequest(inputData):
    try:
        if verboseMode:
            print(GOOD_PREFIX  + " received " + str(inputData))
            print(GOOD_PREFIX + " sending data ...")
        #if inputData['forward'] == 1:
        #    pass
        #if inputData
        emit("data", generateData())
    except:
        quit()

def generateData():
    return {"temperature":getTemperature(), 
            "CPU": getCpuUsage(), 
            "flashlight": featuresStates["flashlight"], 
            "laser": featuresStates["laser"],
            "buzzing": featuresStates["buzzing"]} 

def getTemperature():
    #info = psutil.sensors_temperatures()['coretemp']
    ret = 0
    #for cpuinfo in info:
    #    ret =  max(ret,cpuinfo.current)
    return ret  

def getCpuUsage():
    return psutil.cpu_percent()  

###############################################
# functions that respond to user button input #
#                                             #
@socketio.on("laser")
def switchLaser():
    if verboseMode:
        featuresStates["laser"] = not featuresStates["laser"]
        if featuresStates["laser"]:
            print(GREEN_ESCAPE + u"{*} laser on" + ESCAPE_END) 
        else:
            print(RED_ESCAPE + "{*} laser off" + ESCAPE_END)

@socketio.on("flashlight")
def switchFlashlight():
    if verboseMode:
        featuresStates["flashlight"] = not featuresStates["flashlight"]
        if featuresStates["flashlight"]:
            print(GREEN_ESCAPE + u"{*} flashlight on" + ESCAPE_END) 
        else:
            print(RED_ESCAPE + "{*} flashlight off" + ESCAPE_END)

@socketio.on("buzz")
def buzz():
    if verboseMode:
        featuresStates["buzzing"] = not featuresStates["buzzing"]
        if featuresStates["buzzing"]:
            print(GREEN_ESCAPE + u"{*} buzzing on" + ESCAPE_END) 
        else:
            print(RED_ESCAPE + "{*} buzzing off" + ESCAPE_END)

################################################################################    
# CONTROLLER CLASS
class controller():
    @staticmethod
    def configurate():
        global args, verboseMode
        # get user input
        parser = argparse.ArgumentParser(description="Python program that runs flask server that controls raspi-bot")
        parser.add_argument("--verbose",action="store_true", help="verbose output")
        args = parser.parse_args()

        if args.verbose is not None:
            verboseMode = True

        # if streaming is available then config camera
        if couldStream:
            Camera.camera.resolution   = DEF_RESOLUTION
            Camera.camera.image_effect = DEF_EFFECT
            Camera.camera.framerate    = DEF_FRAMERATE

        # if electronics are enabled then configurate them
        if electronicsEnabled:
            electronicSetup()
            

    @staticmethod
    def start():
        global isServingFiles

        try :
            if args.verbose is not None:
                print(GOOD_PREFIX + u"starting server")            
            
            socketio.run(app, host='0.0.0.0' )
        except (KeyboardInterrupt, SystemExit):
            isServingFiles = False

            if args.verbose is not None:
                print(WARNING_PREFIX + "Exiting app")
            print("Bye !")
            sys.exit(0)

################################################################################    

if __name__ == '__main__':
    controller.configurate()
    controller.start()
