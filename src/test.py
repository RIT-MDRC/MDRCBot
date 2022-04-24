from gpiozero import Servo
from time import sleep

PINOUTS = {
    18 : "BOARD18",
    16: "BOARD16",
    7: "BOARD7",
    11: "BOARD11",
    13: "BOARD13",
    15: "BOARD15",
    29: "BOARD29", #right
    31: "BOARD31", # left
    33: "BOARD33", # Eyes
    22: "BOARD22" # Audio
}

servo = Servo(PINOUTS[31])

while True:
    #servo.min()
    sleep(0.5)
    servo.mid()
    sleep(0.5)
