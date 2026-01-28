encoder_1 = Encoder(brain.three_wire_port.a)

def degree_tracker(old_position):
    position = encoder_1.position(DEGREES)
    position = position - old_position
    return position

def distance_tracker():
    distance = 0
# replace with actual circumference of the wheels
    ccircumference = 0
    i = 0
    old_position = 0
    while i < 30:
        degree_tracker(old_position)
        distance += position/distance*circumference
        old_position = old-position + position 
        i+=1
        brain.screen.print(distance)
    if i = 30:
        i=0

