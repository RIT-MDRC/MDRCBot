# Project Name: MDRCBot
# Author: Cameron Robinson
# Email: cvr8924@rit.edu
# Date: 10/10/21
# Description Onboard code for Raspberry Pi Running inside personality robot constructed over october break 2021

import gpiozero as gpio
from time import sleep
import sys

########################################
### Declarations ###

## Input ##
# Button #
headButton = gpio.Button("BOARD37")
# IR #
FrontIR = gpio.MotionSensor("BOARD16")
BottomIR = gpio.MotionSensor("BOARD18")

## Output ##
# LED #
leftRedLed = gpio.LED("BOARD7")
leftWhiteLed = gpio.LED("BOARD11")
rightRedLed = gpio.LED("BOARD13")
rightWhiteLed = gpio.LED("BOARD15")


# Servo #
# rightArmServo = gpio.AngularServo("BOARD29")
# leftArmServo = gpio.AngularServo("BOARD31")
# eyesServo = gpio.AngularServo("BOARD33")
# Speaker
# speaker = gpio.TonalBuzzer("BOARD22")
########################################


def happy_behavior():
    print("happy")
    leftWhiteLed.on()
    rightWhiteLed.on()
    rightRedLed.on()
    leftRedLed.on()

def angry_behavior():
    print("angry")
    rightRedLed.on()

def sleep_behavior():
    print("sleep")

def idle_behavior():
    print("idle")


# Main: Executes at runtime
if __name__ == '__main__':
    #happy_behavior()
    for i in range(100):
        rightRedLed.on()
        leftRedLed.on()
        leftWhiteLed.on()
        rightWhiteLed.on()
        sleep(1)
        rightRedLed.off()
        leftRedLed.off()
        leftWhiteLed.off()
        rightWhiteLed.off()
        sleep(1)


