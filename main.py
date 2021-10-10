# Project Name: MDRCBot
# Author: Cameron Robinson
# Email: cvr8924@rit.edu
# Date: 10/10/21
# Description Onboard code for Raspberry Pi Running inside personality robot constructed over october break 2021

import gpiozero
import time
import sys



def happy_behavior():
    print("happy")

def angry_behavior():
    print("angry")

def sleep_behavior():
    print("sleep")

def idle_behavior():
    print("idle")


# Main: Executes at runtime
if __name__ == '__main__':
    print("Start Up")

