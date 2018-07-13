from microbit import *

####################################################
def robot_stop():
    pin2.write_digital(0)
    pin1.write_digital(0)
    pin0.write_digital(0)
#END robot_stop()

#####################################################
def robot_right():
    pin2.write_digital(1)
    pin1.write_digital(0)
    pin0.write_digital(0)
#END robot_right()

#####################################################
def robot_fwd():
    pin2.write_digital(0)
    pin1.write_digital(0)
    pin0.write_digital(1)
#END robot_fwd()

#####################################################
def tell_robot(turn_count, distance):

    #execute turn_count right turns
    for count in range(turn_count):
        robot_right()
        robot_stop()

    #mv forward distance times
    for increment in range(distance):
        robot_fwd()
        robot_stop()
        
# END tell_robot

display.scroll("Hello")
while True:
    #turn right
    if button_a.was_pressed():
        display.scroll("r")
        robot_right()
        robot_stop()
    elif button_b.was_pressed():
        display.scroll("F")
        robot_fwd()
        robot_stop()
    
    #pin2.write_digital(0)
    #pin1.write_digital(0)
    #pin0.write_digital(0)
    
