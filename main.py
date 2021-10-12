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
rightArmServo = gpio.AngularServo("BOARD29") #90 degrees (fuzzy) ~CR
leftArmServo = gpio.AngularServo("BOARD31")  #90 degrees (fuzzy) ~CR
eyesServo = gpio.AngularServo("BOARD33")     #60 degrees (fuzzy) ~CR
# Speaker
speaker = gpio.TonalBuzzer("BOARD22", None, gpio.tones.Tone('A4'), 3)  # configures the buzzer to accept 7 octave span


########################################


def happy_behavior():
    print("happy")


def angry_behavior():
    print("angry")
    rightRedLed.on()


def sleep_behavior():
    print("sleep")

    # Shutdown tone
    speaker.play(gpio.tones.Tone(midi=82))
    sleep(0.5)
    speaker.stop()
    sleep(0.05)
    speaker.play(gpio.tones.Tone(midi=72))
    sleep(0.5)
    speaker.stop()

    # Shut Downs:
    speaker.stop()

    rightRedLed.off()
    rightWhiteLed.off()
    leftRedLed.off()
    leftWhiteLed.off()

    rightArmServo.value = None
    leftArmServo.value = None
    eyesServo.value = None


def idle_behavior():
    print("idle")

    # Set Values
    rightWhiteLed.on()
    leftWhiteLed.on()

    # DECIDE: Do we want to hold a position?
    rightArmServo.value = None
    leftArmServo.value = None
    eyesServo.value = None

    # Shut Downs
    speaker.stop()

    rightRedLed.off()
    leftRedLed.off()


def test_behavior():  # test routine, should never run in main program ~CR
    # happy_behavior()
    for i in range(100):
        rightRedLed.on()
        leftRedLed.on()
        leftWhiteLed.on()
        rightWhiteLed.on()
        print(FrontIR.value)
        print(BottomIR.value)

        # speaker.play(gpio.tones.Tone(midi = 37)) # sample tone

        sleep(1)
        rightRedLed.off()
        leftRedLed.off()
        leftWhiteLed.off()
        rightWhiteLed.off()
        print(FrontIR.value)
        print(BottomIR.value)
        sleep(1)


# Main: Executes at runtime
if __name__ == '__main__':
    sleep_behavior()

