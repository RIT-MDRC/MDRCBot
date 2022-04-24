""" MDRC Bot now with new and improved emotions

Project Name:
    MDRC Bot
Authors:
    Cameron Robinson (cvr8924@rit.edu)
    Clinten Hopkins (cmh3586@rit.edu)
Maintainers:
    Clinten Hopkins (cmh3586@rit.edu)
Last Updated:
    4/23/21
Description:
    Created a version of the MDRC Bot to allow for angry emotions in addition to the pre-existing idle and wave actions
Version:
    1.1
"""

from gpiozero import Servo, MotionSensor, LED, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

########################################
### Declarations ###
## Globals ##
PINOUTS = {
    "F_IR" : "BOARD18",
    "B_IR": "BOARD16",
    "LR_LED": "BOARD7",
    "LW_LED": "BOARD11",
    "RR_LED": "BOARD13",
    "RW_LED": "BOARD15",
    "R_SERVO": "BOARD29",
    "L_SERVO": "BOARD31",
    "EYES_SERVO": "BOARD33",
    "SPEAKER": "BOARD22"
}

## Input ##
# IR #
FrontIR = MotionSensor(PINOUTS["F_IR"])
BottomIR = MotionSensor(PINOUTS["B_IR"])

## Output ##
# LED #
leftRedLed = LED(PINOUTS["LR_LED"])
leftWhiteLed = LED(PINOUTS["LW_LED"])
rightRedLed = LED(PINOUTS["RR_LED"])
rightWhiteLed = LED(PINOUTS["RW_LED"])

# Servo #
rightArmServo = Servo(PINOUTS["R_SERVO"])
leftArmServo = Servo(PINOUTS["L_SERVO"])
eyesServo = Servo(PINOUTS["EYES_SERVO"])

# Speaker #
# speaker = TonalBuzzer(PINOUTS["SPEAKER"], None, Tone('A4'), 3)

########################################

def wave_behavior() -> None:
    """
    Sets the eyes to white (turn off red and turn on white) and then move the right arm towards the head and back down 3
    times

    :return: None
    """
    # print(f"hello\n\tIR : {IR.value}")
    rightWhiteLed.on()          # Turn the eyes white
    leftWhiteLed.on()
    rightRedLed.off()
    leftRedLed.off()

    eyesServo.min()             # Set eyes to happy

    for _ in range(3):
        rightArmServo.min()     # Wave left
        sleep(0.5)              # Let it sit there for a little bit
        rightArmServo.mid()     # Wave right
        sleep(0.5)              # Let it sit there for a little bit

    eyesServo.detach()          # Dont try to hold that position
    rightArmServo.detach()

def angry_behavior() -> None:
    """
    Sets the eyes to red (turn on red and turn off white) and then move both arms towards the head and back down 3 times

    :return: None
    """
    # print(f"angry\n\tIR : {BottomIR.value}")

    rightRedLed.on()            # Turn the eyes red
    leftRedLed.on()
    rightWhiteLed.off()
    leftWhiteLed.off()

    eyesServo.mid()             # Set eyes to happy

    for _ in range(3):          # Loop 3 times
        rightArmServo.min()     # Throw right arm left
        leftArmServo.min()      # Throw left arm right
        sleep(0.5) 
        rightArmServo.mid()     # Throw right arm right
        leftArmServo.mid()      # Throw left arm left
        sleep(0.5)              # Let it sit there for a little bit

    eyesServo.detach()          # Dont try to hold that setpoint
    rightArmServo.detach()      # Dont try to hold those positions
    leftArmServo.detach()

def idle_behavior() -> None:
    """
    Basic behavior to reset the eyes (turn on the white and turn off the red) and let the arms just rest at their last
    positions

    :return: None
    """
    
    rightWhiteLed.on()          # Give Default Eyes
    leftWhiteLed.on()
    rightRedLed.off()
    leftRedLed.off()
    
    rightArmServo.detach()      # Stop trying to go to a position
    leftArmServo.detach()
    eyesServo.detach()

def main() -> None:
    """
    Main process to loop thorough the sensors, and if a change to any of them is detected, do the respective action:
        - Change to bottom IR sensor -> angry behavior
        - Change to front IR sensor -> wave behavior
        - No change -> idle behavior

    :return: None
    """
    
    leftArmServo.mid() # Put the arms down
    rightArmServo.mid()
    
    lastFrontIR = FrontIR.value # Set default IR values
    lastBotIR = BottomIR.value
    
    while True:
        if lastBotIR != BottomIR.value:
            angry_behavior()
            lastBotIR = BottomIR.value
        elif lastFrontIR != FrontIR.value:
            wave_behavior()
            lastFrontIR = FrontIR.value
        else:
            idle_behavior()


# Executes at runtime
if __name__ == '__main__':
    main()
