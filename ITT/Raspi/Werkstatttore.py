import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

Inputs = [2,3,4,17]
Outputs = [14,15,23,24]

for i in range(4):
    GPIO.setup(Inputs[i],GPIO.IN)

for i in range(4):
    GPIO.setup(Outputs[i], GPIO.OUT)

while True:
    for i in range(4):
        if GPIO.input(Inputs[i])==GPIO.HIGH:
            GPIO.output(Outputs[i],GPIO.HIGH)
        else:
            GPIO.output(Outputs[i],GPIO.LOW)
    time.sleep(1)