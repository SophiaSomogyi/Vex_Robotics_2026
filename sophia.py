#region VEXcode Generated Robot Configuration
from vex import *
import urandom
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code
motor_1 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
motor_3 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, True)
motor_6 = Motor(Ports.PORT6, GearSetting.RATIO_18_1, True)
distance_20 = Distance(Ports.PORT20)
optical_12 = Optical(Ports.PORT12)
distance_21 = Distance(Ports.PORT21)


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
# 	Project:
#	Author:
#	Created:
#	Configuration:
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code

# VARIABLE DECLARATIONS HERE - check if it's the right spot - should it be inside the pre auto??
teamColor = "red"
enemyColor = "blue"
ballFound = 0
ballRotationNum = 0 

def pre_autonomous(): # part of template
    # actions to do when the program starts
    brain.screen.clear_screen() # part of template
    brain.screen.print("pre auton code") # part of template
    wait(1, SECONDS) # part of template

    # brain should be defined by default 
    brain=Brain()

    # PORTS CONFIGURATION (from Michelle)

    # motors for movement
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
    distanceTop = Distance(Ports.PORT20) # CHANGE PORT NUM
    distanceBottom = Distance(Ports.PORT21) #CHANGE PORT NUM

    # pneumatics - do we need this??
    pneumatics = DigitalOut(brain.three_wire_port.a)

    #* directions assuming we start on the RIGHT side


def autonomous(): # part of template
    brain.screen.clear_screen() # part of template
    brain.screen.print("autonomous code") # part of template

    global ballFound

    
    # drive right until tube of balls located, then stop moving and exit while loop 
    while ballFound == 0:
        if distanceTop.object_distance(MM) < 100 and optical_12.color() = Color.RED: #HAVE TO CHANGE TEAMCOLOR AND THE DISTANCE AMOUNT
            stopDriveMotors()
            ballFound = 1
        else:
            driveRight()

    # drive forward until object close
    driveToObject()

    #HAVE TO ALIGN / MAKE SURE IT'S ALIGNED!! 
    alignWithBall() # not made yet
    
    # THIS LOOP NEEDS WORK
    # SUPPOSED TO MAKE SURE THAT THE BALLS ACTUALLY TO GET PICKED UP
    # SO IT DOESN'T MOVE ON THINKING IT HAS THEM WHEN IT DIDN'T GRAB ANYTHING 
    while collectTeamBallTube(3) == "ERROR": # should pick up up 3 balls, recieves an error message if the color is not detected indicating that the ball isn't in correct position
        alignWithBall()
        collectTeamBallTube(3)
    #FUNCTION RELATED TO THE LIMIT SWITCH / COUNTING THE BALL INTAKE GOES HERE SOMEWHERE (could repalace the other color check in collectTeamBall fn) 
    
    #rotate robot 180 degrees here (turns around)
    turnRight(5) #CHANGE - find out how many rotations for 360, /2 for 180 and /4 for 45. 
    # would be best to find this mathematically to be precise as possible...  d / c?? 

    #moving from tube to long goal then stop 
    while distanceBottom.object_distance(MM) > 10:
        driveForward()
    stopDriveMotors()

    #ALIGN WITH GOAL FUNCTION HERE
    alignWithGoal() # not completed yet

    #Outputs balls from storage into correct goal 
    outputTeamBall(3)

    #Drives to other ball location 
    #instead of turning, use hdrive to move sideways because then it will be facing the correct way
    #PUT THIS INTO A FUNCTION (USED PART OF IT TWICE)
    ballFound = 0
    while ballFound == 0:
        if distanceTop.object_distance(MM) < 100 and optical_12.color() = Color.RED: #HAVE TO CHANGE TEAMCOLOR AND THE DISTANCE AMOUNT
            stopDriveMotors()
            ballFound = 1
        else:
            driveLeft() #CHANGE FOR OTHER FILE 

    #Intake balls x3
    collectTeamBallTube(3)

    #should be stopped at this point
    stopAllMotors()
   
    #Drive to short goal
    #Turn 45 degrees 
    turnLeftRotations(3) #Change left to right, figure out correct number (360 / 8 = 45)
    #drives forward until close to object 
    driveToObject()

    # align with short goal
    alignWithGoal()

    #Outputs team balls 
    outputTeamBall(3)


# # #  MOVEMENT FUNCTIONS # # # 

# moves forward - both left and right drive 

# indefinitely 
def driveForward():
    brain.screen.print("drive forward indefinitely") #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(FORWARD)

# take amount of rotations, speed, and if it blocks the script (True) or not (False)
def driveForwardRotations(veclocity, numRotations, waitValue):
    brain.screen.print("drive forward, velocity = " + velocity + " rotations = " + numRotations) #update console 
    leftDrive.set_velocity(veclocity, PERCENT)
    rightDrive.set_velocity(veclocity, PERCENT)
    leftDrive.spin_for(FORWARD, numRotations, TURNS, wait = waitValue)
    rightDrive.spin_for(FORWARD, numRotations, TURNS, wait  waitValue)

# moves backward - both left and right drive 
# indefinitely
def driveBackward():
    brain.screen.print("drive backward indefinitely") #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(REVERSE)
    rightDrive.spin(REVERSE)

# amount of rotations
def driveBackwardRotations(numRotations):
    brain.screen.print("drive backward, rotations = " + numRotations) #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin_for(REVERSE, numRotations, TURNS)
    rightDrive.spin_for(REVERSE, numRotations, TURNS)

# moves right - just Hdrive
# indefinitely
def driveRight():
    brain.screen.print("drive right indefinitely") #update console
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(FORWARD)

# amount of rotations
def driveRightRotations(numRotations):
    brain.screen.print("drive right, rotations = " + numRotations) #update console
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin_for(FORWARD, numRotations, TURNS)

# moves left - just Hdrive 
# indefinitely
def driveLeft():
    brain.screen.print("drive left indefinitely") #update console
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin(REVERSE)

# amount of rotations
def driveLeftRotations():
    brain.screen.print("drive left, rotations = " + numRotations) #update console
    hdrive.set_velocity(100, PERCENT)
    hdrive.spin_for(REVERSE, numRotations, TURNS)

# turns right - both right and left drive
# indefinitely
def turnRight():
    brain.screen.print("turn right indefinitely") #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(FORWARD)
    rightDrive.spin(REVERSE)

# amount of rotations
def turnRightRotations(numRotations):
    brain.screen.print("turn right, rotations = " + numRotations) #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin_for(FORWARD, numRotations, TURNS)
    rightDrive.spin_for(REVERSE, numRotations, TURNS)

# turns left  - both right and left drive
# indefinitely
def turnLeft():
    brain.screen.print("turn left indefinitely") #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin(REVERSE)
    rightDrive.spin(FORWARD)

# amount of rotations
def turnLeftRotations(numRotations):
    brain.screen.print("turn left, rotations = " + numRotations) #update console
    leftDrive.set_velocity(100, PERCENT)
    rightDrive.set_velocity(100, PERCENT)
    leftDrive.spin_for(REVERSE, numRotations, TURNS)
    rightDrive.spin_for(FORWARD, numRotations, TURNS)

# stops all motors that control wheels - left and right and hdrive 
def stopDriveMotors():
    brain.screen.print("stop drive motors") #update console 
    hdrive.stop()
    leftDrive.stop()
    rightDrive.stop()


# # # BALL CONTROL FUNCTIONS # # #

# # MOTORS # # 

# motor movement to store balls of the correct color
def storeTeamBall(numRotations):
    global myVariable
    # velocity 
    colourMotor.set_velocity(100, PERCENT)
    top.set_velocity(0, PERCENT)
    middle.set_velocity(100, PERCENT)
    bottom.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    colourMotor.spin_for(REVERSE, numRotations, TURNS)
    middle.spin_for(FORWARD, numRotations, TURNS)
    bottom.spin_for(FORWARD, numRotations, TURNS)
    backIntake.spin_for(REVERSE, numRotations, TURNS)


# motor movement to store enemy balls
def storeEnemyBall(numRotations):
    # velocity
    colourMotor.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    leftDrive.set_velocity(100, PERCENT)
    colourMotor.set_velocity(100,PERCENT)
    # direction
    backIntake.spin_for(REVERSE, numRotations, TURNS)
    middle.spin_for(FORWARD, numRotations, TURNS)
    bottom.spin_for(FORWARD, numRotations, TURNS)
    colourMotor.spin_for(FORWARD, numRotations, TURNS)

    #colourMotor.spin_for(FORWARD, 90, DEGREES) - what michelle had 

# motor movement to output balls into the long goal 
def longGoal(numRotations):
    global myVariable
    # velocity
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    top.spin_for(REVERSE, numRotations, TURNS)
    middle.spin_for(FORWARD, numRotations, TURNS)
    bottom.spin_for(FORWARD, numRotations, TURNS)
    backIntake.spin_for(REVERSE, numRotations, TURNS)

# motor movement to output balls into the short goal 
def shortGoal(numRotations):
    global myVariable
    # velocity
    bottom.set_velocity(100, PERCENT)
    middle.set_velocity(100, PERCENT)
    top.set_velocity(0, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    # direction
    middle.spin_for(REVERSE, numRotations, TURNS)
    bottom.spin_for(FORWARD, numRotations, TURNS)
    backIntake.spin_for(REVERSE, numRotations, TURNS)

# motor movement to take balls out of storage, must happen before short/long goal output
def takeOut(numRotations): # leave storage 
    global myVariable
    # velocity
    colourMotor.set_velocity(100, PERCENT)
    backIntake.set_velocity(100, PERCENT)
    bottom.set_velocity(70, PERCENT)
    colourMotor.spin_for(REVERSE, numRotations, TURNS)
    backIntake.spin_for(FORWARD, numRotations, TURNS)
    bottom.spin_for(FORWARD, numRotations, TURNS)

# stops motors that control ball movement
def stopBallMotors():
    bottom.stop()
    middle.stop()
    top.stop()
    backIntake.stop()
    colourMotor.stop()

# checks that the ball has been correctly identified and located with the color sensor
# then intakes the balls from the tube in one shot by rotating the correct motors
def collectTeamBallTube(numberOfBalls):
    # TEST THIS ONE SEPARATELY - HAVE TO MAKE SURE THE COLOR SENSOR IS RELIABLE
    # ALSO SEE IF IT NEEDS TO BE MOVING FWD AT THE SAME TIME & WHAT SPEED
    if optical_12.color() == Color.RED:
        driveForwardRotations(20, 5, False) # moves fwd at 20% speed, 5 (change) motor rotations and it will not block the rest of the fn from going as it does 
        brain.screen.print("Red Ball Collecting") #update console
        storeTeamBall(numberOfBalls * ballRotationNum) # number of balls x amount to rotate per 1 ball = total rotation amount 
        brain.screen.print(numberOfBalls + " x " + ballRotationNum + ", collected team balls") # update console / check values are correct
        return("COMPLETE")
    else:
        return("ERROR") # ball not found

#collect the balls free on the ground - will have to re-align each time with each ball
def collectTeamBallGround(numberOfBalls):
    i = numberOfBalls
    while i > 0:
        #ADD SOME SORT OF FAIL SAFE HERE TO MAKE SURE THAT THEY ACTUALLY GO IN, IF NOT THEN FIX ALIGNMENT
        alignWithBall() 
        #do we need to stop motors here? 
        driveForwardRotations(20, 5, False) # moves fwd at 20% speed, 5 (change) motor rotations and it will not block the rest of the fn from going as it does 
        storeTeamBall(ballRotationNum)
        wait(0.2,SECONDS) #pause so nothing gets messed up - check if time's good
        i -= 1


# collects enemy balls 
# don't think we need this fn but just in case
def collectEnemyBall(): 
    if optical_12.color() == Color.BLUE: #CHANGE THIS 
        brain.screen.print("Enemy ball found")
        storeEnemyBall(ballRotationNum) # change amount 
    else:
        return("ERROR")


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

#moves forward indefinitely until it is less than 10 mm from object, then stops drive motors
def driveToObject():  
    while distanceBottom.object_distance(MM) > 10:
        driveForward()
    stopDriveMotors()



# # BALL WITH GOAL CONTROL # # 

#function to sort balls according to color 
# NOT CURRENTLY USED IN MAIN
def sortBall():
    if checkColor() == teamColor:
        #check if space
        #move motors correctly to place into hold

    else if checkColor() == opponentColor:
        #check if space
        #move motors correctly to place into hold 
    

# determines if output long or short goal based on distance sensors, returns which goal 
def whichGoal():
    # checks if the robot is aligned with the long goal 
    if distanceTop.object_distance(MM) < 5: # will have to change  this amount 
        brain.screen.print("Goal selected: long") #update console
        return "longGoal"
        
    # checks if the robot is NOT aligned with the long goal and is therefore aligned with the short goal
    else if distanceBottom.object_distance(MM) > 5: # will have to change this amount 
        brain.screen.print("Goal selected: short") #update console
        return "shortGoal"

    else: #error message - tells the robot that it needs to readjust?
        brain.screen.print("No goal found!") #update console 
        return "noGoal" 

# outputs team balls from storage to the correct goal 
def outputTeamBall(numBalls):
    i = numBalls # incrementation for loop, that it will go # times that corresponds to # balls in storage
    # -
    if whichGoal() == "longGoal":
        while i > 0:
            takeOut(ballRotationNum) 
            wait(0.2,SECONDS) #pause so nothing gets messed up - check if time's good
            longGoal(ballRotationNum)
            wait(0.2,SECONDS) #pause so nothing gets messed up - check if time's good
            i -= 1
    else if whichGoal() == "shortGoal":
        while i > 0:
            takeOut(ballRotationNum) 
            wait(0.2,SECONDS) #pause so nothing gets messed up - check if time's good
            shortGoal(ballRotationNum)
            wait(0.2,SECONDS) #pause so nothing gets messed up - check if time's good
            i -= 1
    else if whichGoal() == "noGoal": 
        pass 
        #have to realign - goal not detected 
        #change this 
    else:
        brain.screen.print("OUTPUT_BALL_ERROR") 

# # # ALIGNMENT FUNCTIONS # # # 

def alignWithBall():
    pass 
    #going to have to be something like it slowly rotates 
    #right or left until it reaches the correct position to pick up the ball
    #color sensor and distance sensor - but how exactly? 

def alignWithGoal():
    pass
    #distance in the x should be ~= on both sides, would that work?

# might need this? could be good just in case - specifically for testing (change)
def printCursorControl():
    pass

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

# delete this when going back to template 
pre_autonomous()
autonomous()