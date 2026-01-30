#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


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
# 	Project:
#	Author:
#	Created:
#	Configuration:
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

def pre_autonomous(): # part of template
    # actions to do when the program starts
    brain.screen.clear_screen() # part of template
    brain.screen.print("pre auton code") # part of template
    wait(1, SECONDS) # part of template

    # brain should be defined by default 
    brain=Brain()

    # PORTS CONFIGURATION (from Michelle)

    # motos for movement
    leftDrive = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
    rightDrive = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
    hdrive = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)

    # motors for ball mechanism 
    bottom = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
    middle = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
    top = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
    colourMotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
    backIntake = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)

    # optical sensor 
    optical_12 = Optical(Ports.PORT12)
    # distance sensor here
    # distance sensor here 

    # pheumatics - do we need this??
    pneumatics = DigitalOut(brain.three_wire_port.a)

    # VARIABLE DECLARATIONS HERE 


def autonomous(): # part of template
    brain.screen.clear_screen() # part of template
    brain.screen.print("autonomous code") # part of template





# # #  MOVEMENT FUNCTIONS # # # 

# moves forward - both left and right drive 
def driveForward():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)

# moves backward - both left and right drive 
def driveBackward():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(REVERSE)
    rightDrive.spin(REVERSE)

# moves right - just Hdrive
def driveRight():
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(FORWARD)

# moves left - just Hdrive 
def driveLeft():
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(REVERSE)

# moves diagonally forward and right - left and right drive and hdrive 
def driveForwardRight():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    hdrive.set_velocity(100, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)
    hdrive.spin(FORWARD)

# moves diagonally forward and left - left and right drive and hdrive 
def driveForwardLeft():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    hdrive.set_velocity(100, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)
    hdrive.spin(REVERSE)

# moves diagonally backward and right - left and right drive and hdrive 
def driveBackwardRight():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    hdrive.set_velocity(100, PERCENT)
    leftDrive.spin(REVERSE)
    rightDrive.spin(REVERSE)
    hdrive.spin(FORWARD)

# moves diagonally backward and left - left and right drive and hdrive 
def driveBackwardLeft():
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    hdrive.set_velocity(100, PERCENT)
    leftDrive.spin(REVERSE)
    rightDrive.spin(REVERSE)
    hdrive.spin(REVERSE)

# stops all motors that control wheels - left and right and hdrive 
def stopDriveMotors():
    hdrive.stop()
    leftDrive.stop()
    rightDrive.stop()


# # # BALL CONTROL FUNCTIONS # # #

# motor movement to store balls of the correct color
def storeTeamBall():
    global myVariable
    # velocity 
    colourMotor.set_velocity(100, PERCENT)
    top.set_velocity(0, PERCENT)
    middle.set_velocity(100, PERCENT)
    bottom.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    colourMotor.spin(REVERSE)
    middle.spin(FORWARD)
    bottom.spin(FORWARD)
    backIntake.spin(REVERSE)

# motor movement to store enemy / opponent balls
def storeEnemyBall():
    # velocity
    colourMotor.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    colourMotor.set_velocity(100,PERCENT)
    # direction
    backIntake.spin(REVERSE)
    middle.spin(FORWARD)
    bottom.spin(FORWARD)
    colourMotor.spin(FORWARD)
    #colourMotor.spin_for(FORWARD, 90, DEGREES) - what michelle had 

# motor movement to output balls into the long goal 
def longGoal():
    global myVariable
    # velocity
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    top.spin(REVERSE)
    middle.spin(FORWARD)
    bottom.spin(FORWARD)
    backIntake.spin(REVERSE)

# motor movement to output balls into the short goal 
def shortGoal():
    global myVariable
    # velocity
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(0, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    middle.spin(REVERSE)
    bottom.spin(FORWARD)
    backIntake.spin(REVERSE)

# motor movement to take balls out of storage, must happen before short/long goal output
def takeOut(): # / leave storage 
    global myVariable
    # velocity
    colourMotor.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    bottom.set_velocity(70, PERCENT)
    colourMotor.spin(REVERSE)
    backIntake.spin(FORWARD)
    bottom.spin(FORWARD)

# stops motors that control ball movement
def stopBallMotors():
    bottom.stop()
    middle.stop()
    top.stop()
    backIntake.stop()
    colourMotor.stop()

# stops all motors 
def stopAllMotors():
    hdrive.stop()
    leftDrive.stop()
    rightDrive.stop()
    bottom.stop()
    middle.stop()
    top.stop()
    backIntake.stop()
    colourMotor.stop()


"""
FROM TEMPLATE: 

def user_control():
    brain.screen.clear_screen()
    # place driver control in this while loop
    while True:
        wait(20, MSEC)

# create competition instance
comp = Competition(user_control, autonomous)
pre_autonomous()
"""