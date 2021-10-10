# Project Name: MDRCBot
# Author: Cameron Robinson
# Email: cvr8924@rit.edu
# Date: 10/10/21
# Description Onboard code for Raspberry Pi Running inside personality robot constructed over october break 2021

import gpiozero as gpio
import time
import sys

########################################
### Declarations ###

## Input ##
# Button #
headButton = Button("BOARD37")
# IR #
FrontIR  = MotionSensor("BOARD16")
BottomIR = MotionSensor("BOARD18")

## Output ##
# LED #
leftRedLed = LED("BOARD7")
leftWhiteLed = LED("BOARD11")
rightRedLed = LED("BOARD13")
rightWhiteLed = LED("BOARD15")
# Servo #
rightArmServo = AngularServo("BOARD29")
leftArmServo = AngularServo("BOARD31")
eyesServo = AngularServo("BOARD33")
# Speaker
speaker = TonalBuzzer("BOARD22")
########################################


def happy_behavior():
    print("happy")
    leftWhiteLed.on()
    rightWhiteLed.on()

def angry_behavior():
    print("angry")

def sleep_behavior():
    print("sleep")

def idle_behavior():
    print("idle")


# Main: Executes at runtime
if __name__ == '__main__':
    happy_behavior()

