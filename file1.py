#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
optical_1 = Optical(Ports.PORT1)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


# Color to String Helper
def convert_color_to_string(col):
    if col == Color.RED:
        return "red"
    if col == Color.GREEN:
        return "green"
    if col == Color.BLUE:
        return "blue"
    if col == Color.WHITE:
        return "white"
    if col == Color.YELLOW:
        return "yellow"
    if col == Color.ORANGE:
        return "orange"
    if col == Color.PURPLE:
        return "purple"
    if col == Color.CYAN:
        return "cyan"
    if col == Color.BLACK:
        return "black"
    if col == Color.TRANSPARENT:
        return "transparent"
    return ""

def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# ASSIGNING PORTS 
optical_sensor = Optical(Ports.PORT1)
motor_1 = Motor(Ports.PORT2)



# Begin project code

def start():
    i = 1
    brain.screen.print("Start!")
    brain.screen.clear_screen()
    optical_sensor.set_light_power(70, PERCENT)

    cursorLine = 1;
    while i < 30:
        brain.screen.set_cursor(cursorLine, 1)
        checkColor()
        wait(1, SECONDS)
        i += 1
        # text goes to the next line
        cursorLine += 1 
        # resets the screen when it is full
        if cursorLine == 12:
            brain.screen.clear_screen()
            cursorLine = 1

# function to check the color, if it is red or blue that is the output, if not it is "no color"
def checkColor():
    if optical_sensor.color() == Color.RED:
        brain.screen.print("Red Object")
        moveMotor(FORWARD)
    elif optical_sensor.color() == Color.BLUE:
        brain.screen.print("Blue Object")
        moveMotor(REVERSE)
    else:
        brain.screen.print("No Color")
        moveMotor("none")

# function to move the motor FORWARD or REVERSE

def moveMotor(motorDirection):
    motor_1.spin(motorDirection)

start()

    #brain.screen.print("Timer in Seconds: ", brain.timer.time(SECONDS))
    #brain.screen.clear_screen()
    #brain.screen.set_cursor(1, 1)
