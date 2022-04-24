# Project Name: MDRC Bot

## Author(s)
- Cameron Robinson (cvr8924@rit.edu)
- Ryland Charron (rjc3002@rit.edu)
- Devon Chicchi (dtc3416@rit.edu)
- Clinten Hopkins (cmh3586@rit.edu)

## Maintainer(s)
- Clinten Hopkins (cmh3586@rit.edu)

## Description
Devon, Ryland, and Cameron's Personal Project for a robot w/ personality over the 2021 October break.

## How To Use
- Power on (Once powered on, the boot up process takes a while. If it takes more than 60 seconds, see the troubleshooting section)
    - Plug the power from MDRC Bot into the wall and flip the switch to the on position
- The white LEDs should now be powered on, and you should be able to wave (with a distance of 8-12 inches) and get a 
wave back
- You can now unplug the USB splitter and monitor and as long as it does not lose power, it should stay functional
- Enjoy! :)

## Troubleshooting
Have you tried turning it off and back on again?

### Common Issues:
- [Powered on but not moving](#no-movement)

### No movement
If the bot is powered but nothing is working, plug in a keyboard and monitor to try to manually initiate the program.

When you plug in the periferals, you should see a terminal appear on your screen, assuming the bot is still powered. Once the screen
stabalizes, ie. you see a blinking cursor at the bottom of the screen, you should be able to run `sudo python MDRCBot/src/main.py`. Once
this runs, you should see:

```
Starting...
Setup Complete...
```
 
 and if you wave to it you should see:
 
 ```
 Waving...
 ```
you can now unplug the perifierals and setup the bot for presenting. DO NOT TURN IT OFF at this point. A reboot will NOT automatically
start the program again. 

## Known Issues
- The left eye's white LED has power issues
- The button on top of the bot has some design issues leading to it's non-implementation

## Releases
Please reference SECURITY.md for the currently supported versions of this project. 

|    Date    |                             Version                            |
|:----------:|:--------------------------------------------------------------:|
|  10/10/21  |  [1.0](https://github.com/RIT-MDRC/MDRCBot/releases/tag/v1.0)  |
|   4/24/21  |  [2.0](https://github.com/RIT-MDRC/MDRCBot/releases/tag/v2.0)  |
