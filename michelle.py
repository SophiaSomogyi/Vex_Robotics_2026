#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
leftDrive = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
rightDrive = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
bottom = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
middle = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
top = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
colourMotor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
backIntake = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
optical_12 = Optical(Ports.PORT12)
pneumatics = DigitalOut(brain.three_wire_port.a)
hdrive = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)


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

myVariable = 0

def controller_1buttonR2_pressed_callback_0():
    global myVariable
    # hdriveleft
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(FORWARD)

def controller_1buttonR1_pressed_callback_0():
    global myVariable
    # hdriveright
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(REVERSE)

def controller_1buttonL2_pressed_callback_0():
    global myVariable
    # long goal
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    top.spin(REVERSE)
    middle.spin(FORWARD)
    bottom.spin(FORWARD)
    backIntake.spin(REVERSE)

def controller_1buttonR2_released_callback_0():
    global myVariable
    # releasehdriveleft
    hdrive.set_velocity(0, PERCENT)

def controller_1buttonR1_released_callback_0():
    global myVariable
    # releasehdriveright
    hdrive.set_velocity(0, PERCENT)

def controller_1buttonL1_pressed_callback_0():
    global myVariable
    # short goal
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(0, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    middle.spin(REVERSE)
    bottom.spin(FORWARD)
    backIntake.spin(REVERSE)

def when_started1():
    global myVariable
    # Everything starts off
    optical_12.set_light(LedStateType.ON)
    pneumatics.set(False)
    hdrive.set_velocity(0, PERCENT)
    leftDrive.set_velocity(0, PERCENT)
    bottom.set_velocity(0, PERCENT)
    middle.set_velocity(0, PERCENT)
    top.set_velocity(0, PERCENT)
    colourMotor.set_velocity(0, PERCENT)
    backIntake.set_velocity(0, PERCENT)
    rightDrive.set_velocity(0, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)
    bottom.spin(FORWARD)
    middle.spin(FORWARD)
    top.spin(FORWARD)
    colourMotor.spin(FORWARD)
    backIntake.spin(FORWARD)
    hdrive.spin(FORWARD)

def when_started2():
    global myVariable
    # mario kart drive
    while True:
        while controller_1.buttonY.pressing():
            rightDrive.set_velocity(((controller_1.axis3.position() + controller_1.axis4.position()) * 0.8), PERCENT)
            leftDrive.set_velocity(((controller_1.axis3.position() - controller_1.axis4.position()) * 0.8), PERCENT)
            leftDrive.spin(FORWARD)
            rightDrive.spin(FORWARD)
            wait(5, MSEC)
        while controller_1.buttonX.pressing():
            leftDrive.set_velocity(((controller_1.axis3.position() + controller_1.axis4.position()) * 0.8), PERCENT)
            rightDrive.set_velocity(((controller_1.axis3.position() - controller_1.axis4.position()) * 0.8), PERCENT)
            leftDrive.spin(FORWARD)
            rightDrive.spin(FORWARD)
            wait(5, MSEC)
        while controller_1.buttonB.pressing():
            while leftDrive.velocity(PERCENT) > 0:
                leftDrive.set_velocity((leftDrive.velocity(PERCENT) - 20), PERCENT)
                rightDrive.set_velocity((rightDrive.velocity(PERCENT) - 20), PERCENT)
                wait(5, MSEC)
            wait(5, MSEC)
        wait(5, MSEC)

def controller_1buttonDown_pressed_callback_0():
    global myVariable
    # leave storage
    colourMotor.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    bottom.set_velocity(70, PERCENT)
    colourMotor.spin(REVERSE)
    backIntake.spin(FORWARD)
    bottom.spin(FORWARD)

def when_started3():
    global myVariable
    # storage system
    if optical_12.color() == Color.RED and controller_1.buttonUp.pressing():
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
    elif optical_12.color() == Color.BLUE:
        colourMotor.set_velocity(100, PERCENT)
        leftDrive.set_velocity(100, PERCENT)
        leftDrive.set_velocity(100, PERCENT)
        leftDrive.set_velocity(100, PERCENT)
        colourMotor.spin_for(FORWARD, 90, DEGREES)
        backIntake.spin(REVERSE)
        middle.spin(FORWARD)
        bottom.spin(FORWARD)
    else:
        colourMotor.set_velocity(100, PERCENT)

def controller_1buttonL2_pressed_callback_1():
    global myVariable
    pass

def controller_1buttonL2_pressed_callback_2():
    global myVariable
    # long goal

def controller_1buttonRight_pressed_callback_0():
    global myVariable
    # killswitch
    pneumatics.set(False)
    hdrive.set_velocity(0, PERCENT)
    leftDrive.set_velocity(0, PERCENT)
    bottom.set_velocity(0, PERCENT)
    middle.set_velocity(0, PERCENT)
    top.set_velocity(0, PERCENT)
    colourMotor.set_velocity(0, PERCENT)
    backIntake.set_velocity(0, PERCENT)
    rightDrive.set_velocity(0, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)
    bottom.spin(FORWARD)
    middle.spin(FORWARD)
    top.spin(FORWARD)
    colourMotor.spin(FORWARD)
    backIntake.spin(FORWARD)
    hdrive.spin(FORWARD)

def controller_1buttonUp_pressed_callback_0():
    global myVariable
    pneumatics.set(True)

def controller_1buttonUp_released_callback_0():
    global myVariable
    pneumatics.set(False)

def controller_1buttonRight_released_callback_0():
    global myVariable
    colourMotor.set_velocity(100, PERCENT)
    colourMotor.spin(FORWARD)

# system event handlers
controller_1.buttonR2.pressed(controller_1buttonR2_pressed_callback_0)
controller_1.buttonR1.pressed(controller_1buttonR1_pressed_callback_0)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_0)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_1)
controller_1.buttonL2.pressed(controller_1buttonL2_pressed_callback_2)
controller_1.buttonR2.released(controller_1buttonR2_released_callback_0)
controller_1.buttonR1.released(controller_1buttonR1_released_callback_0)
controller_1.buttonL1.pressed(controller_1buttonL1_pressed_callback_0)
controller_1.buttonDown.pressed(controller_1buttonDown_pressed_callback_0)
controller_1.buttonRight.pressed(controller_1buttonRight_pressed_callback_0)
controller_1.buttonUp.pressed(controller_1buttonUp_pressed_callback_0)
controller_1.buttonUp.released(controller_1buttonUp_released_callback_0)
controller_1.buttonRight.released(controller_1buttonRight_released_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
when_started1()
