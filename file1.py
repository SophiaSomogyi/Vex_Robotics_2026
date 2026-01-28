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

# ASSIGNING PORTS - FROM MICHELLE 

optical_sensor = Optical(Ports.PORT1)
motor_1 = Motor(Ports.PORT2) #colour sensor, back intake

#drivetrain motors
motor_2 = Motor(Ports.PORT3) #left
motor_3 = Motor(Ports.PORT4) #right
motor_4 = Motor(Ports.PORT5) #hdrive

#front intake motors
motor_5 = Motor(Ports.PORT6) #1
motor_6 = Motor(Ports.PORT7) #2
motor_7 = Motor(Ports.PORT8) #3

#back intake motor
motor_8 = Motor(Ports.PORT9)

# Assigning team colors - this should be changed when making separate files !
teamColor = "red"
opponentColor = "blue"

# Begin project code

# main script  
def start():
    #initial commands
    brain.screen.print("Start!")
    brain.screen.clear_screen() #clears the screen 
    optical_sensor.set_light_power(70, PERCENT) #sets the light on the optical sensor - might need to change this 



    # loop that controls the screen output to be on a new line each time and refresh when it gets to the bottom of the screen
    cursorLine = 1
    i = 1
    while i < 30:
        brain.screen.set_cursor(cursorLine, 1) 
        checkColor() #check color fn 
        wait(1, SECONDS)
        i += 1
        # text goes to the next line
        cursorLine += 1 
        # resets the screen when it is full
        if cursorLine == 12:
            brain.screen.clear_screen()
            cursorLine = 1
        
#function to sort balls according to color 
def sortBall():
    if checkColor() == teamColor:
        #check if space
        #move motors correctly to place into hold

    else if checkColor() == opponentColor:
        #check if space
        #move motors correctly to place into hold 
    

# function to check the color, if it is red or blue that is the output, if not it is "no color"
def checkColor():
    if optical_sensor.color() == Color.RED:
        brain.screen.print("Red Object")
        return("Red")
    elif optical_sensor.color() == Color.BLUE:
        brain.screen.print("Blue Object")
        return("Blue")
    else:
        brain.screen.print("No Color")
        moveMotor("none")
        return("NoColor")

# function to move the motor FORWARD or REVERSE

def moveMotor(motorDirection):
    motor_1.spin(motorDirection)

start()


def checktimer():
    if brain.timer.time(SECONDS) == 15:
        brain.screen.print("15 seconds passed")
          

# MOVEMENTS
def moveRight():
    ##

def moveLeft():
    ##

def moveForward():
    ##

def moveBackwards():
    ##

# BALL CONTROL - CHANGE motor_#'s to be correct!!!! 

def storeTeamBall():
    motor_1.spin(REVERSE)
    motor_2.spin(FORWARD)
    motor_3.spin(FORWARD)
    motor_4.spin(REVERSE)
    motor_5.spin(REVERSE)


def storeOpponentBall():
    # n/a motor_1.spin()
    motor_2.spin(FORWARD)
    motor_3.spin(REVERSE)
    motor_4.spin(FORWARD)
    motor_5.spin(REVERSE)

def longGoal():
    motor_1.spin(REVERSE)
    motor_2.spin(FORWARD)
    motor_3.spin(FORWARD)
    motor_4.spin(REVERSE)
    motor_5.spin(REVERSE)

def shortGoal():
    # N/A motor_1.spin()
    motor_2.spin(REVERSE)
    motor_3.spin(FORWARD)
    motor_4.spin(FORWARD)
    motor_5.spin(REVERSE)

def takeOut():
    # N/A motor_1.spin()
    # N/A motor_2.spin()
    # N/A motor_3.spin()
    motor_4.spin(REVERSE)
    motor_5.spin(FORWARD)