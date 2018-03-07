#!/usr/bin/python3
from importlib import import_module
import os
from flask import Flask, render_template, Response

couldStream = True

# Raspberry Pi camera module (requires picamera package)
try:
    from camera_pi import Camera
except ImportError:
    print("didn't find module picamera so streaming from raspberry isn't available !")
    couldStream = False

# create flask app
app = Flask(__name__)

################################################################################
# CONSTANTS
DEF_RESOLUTION = (600,400)
DEF_EFFECT     = "none"
DEF_FRAMERATE  = 15 

################################################################################
@app.route('/')
def robot_controls():
    """Video streaming home page."""
    return render_template('robot_controls.html',streamState=couldStream)
    

################################################################################    
def genStream(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        controller.process(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

################################################################################    
@app.route('/video_feed')
def video_feed():
        if couldStream:
            """Video streaming route. Put this in the src attribute of an img tag."""
            return Response(genStream(Camera()),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
    
################################################################################    
class controller():
    @staticmethod
    def configurate():
        
        # if streaming is available then config camera
        if couldStream:
            Camera.camera.resolution   = DEF_RESOLUTION
            Camera.camera.image_effect = DEF_EFFECT
            Camera.camera.framerate    = DEF_FRAMERATE

    @staticmethod
    def process(frame):
        pass
    
    @staticmethod
    def start():
        app.run(host='0.0.0.0', threaded=True)

if __name__ == '__main__':
    controller.configurate()
    controller.start()
