import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs
Motor1A = 16
Motor1B = 18
Motor1E = 22

Motor2A = 23
Motor2B = 21
Motor2E = 19


def setup():
    # GPIO Numbering
    GPIO.setmode(GPIO.BOARD)

    # All pins as Outputs
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def forward():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)


def backward():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH) 
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)


def right():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)


def left():
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)


def stop():
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        backward()
        sleep(1)
        stop()
    except KeyboardInterrupt:
        destroy()
