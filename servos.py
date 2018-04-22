import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(03, GPIO.OUT)
GPIO.setup(05, GPIO.OUT)

servo1 = GPIO.PWM(3, 50)
servo1.start(0)

servo2 = GPIO.PWM(5, 50)
servo2.start(0)

def setAngle(servo,angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    servo.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    servo.ChangeDutyCycle(0)

try:
    while True:
        setAngle(servo1,0)
        sleep(1)
        setAngle(servo1,180)

        setAngle(servo2, 0)
        sleep(1)
        setAngle(servo2,180)
except:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()
