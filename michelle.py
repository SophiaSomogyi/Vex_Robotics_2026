# ASSIGNING PORTS
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

#function to move drivetrain forward
def robForward():
    motor_2.spin(FORWARD)
    motor_3.spin(FORWARD)
    motor_4.stop(COAST)

def robBackward():
    motor_2.spin(REVERSE)
    motor_3.spin(REVERSE)
    motor_4.stop(COAST)

def robSideLEFT():
    motor_2.stop(COAST)
    motor_3.stop(COAST)
    motor_4.spin(FORWARD)

def robSideRIGHT():
    motor_2.stop(COAST)
    motor_3.stop(COAST)
    motor_4.spin(REVERSE)

def robLEFT():
    motor_2.spin(REVERSE)
    motor_3.spin(FORWARD)
    motor_4.stop(COAST)
  
  def robRIGHT():
    motor_2.spin(FORWARD)
    motor_3.spin(REVERSE)
    motor_4.stop(COAST)

