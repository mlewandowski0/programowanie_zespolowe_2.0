#!/usr/bin/python3

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.preview_fullscreen = False
camera.preview_window=(100, 100, 1000, 800)
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = 'Effect: %s' % effect
    sleep(2)
camera.stop_preview()
