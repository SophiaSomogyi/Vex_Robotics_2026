encoder_1 = Encoder(brain.three_wire_port.a)

def degree_tracker():
    encoder_1.reset_position
    position = encoder_1.position(DEGREES)
    return position

def distance_tracker():
    distance = 0
# replace with actual circumference of the wheels
    circumference = 0
    i = 0
    while i < 30:
        degree_tracker(position_old)
        distance += position/distance*circumference
        i+=1
    if i = 30:
        i=0
