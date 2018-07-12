# Add your Python code here. E.g.
from microbit import *
import radio
###############################################
def calc_num_turns(curr_dir, new_dir):
    if curr_dir == "N" :
        if new_dir == "N" :
            num_turns = 0
        elif new_dir == "E":
            num_turns = 1
        elif new_dir == "S":
            num_turns = 2
        elif new_dir == "W":
            num_turns = 3
    elif curr_dir == "E":
        if new_dir == "N" :
            num_turns = 3
        elif new_dir == "E":
            num_turns = 0
        elif new_dir == "S":
            num_turns = 1
        elif new_dir == "W":
            num_turns = 2
    elif curr_dir == "S":
        if new_dir == "N" :
            num_turns = 2
        elif new_dir == "E":
            num_turns = 3
        elif new_dir == "S":
            num_turns = 0
        elif new_dir == "W":
            num_turns = 1
    elif curr_dir == "W":
        if new_dir == "N" :
            num_turns = 1
        elif new_dir == "E":
            num_turns = 2
        elif new_dir == "S":
            num_turns = 3
        elif new_dir == "W":
            num_turns = 0

    return num_turns
#END calc_num_turns
####################################################

#####################################################
def tell_robot(turn_count, distance):

    #execute turn_count right turns
    for count in range(turn_count):
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)

    #mv forward distance times
    for increment in range(distance):
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
        
# END tell_robot

#######################################3
DONE = False
PAUSE = 100

x_coords_done = False
x_coord = 0
y_coord = 0
current_dir = "N"

# turn the radio on
radio.on()

display.scroll('RX!')
sleep(2000)
display.clear()

while True:
    #Set up current coordinates of the robot
    if button_a.was_pressed():
        x_coord = 0
        y_coord = 0
        display.show(Image.YES)
        get_x_coords = True
        while get_x_coords :
            if button_b.was_pressed():
                x_coord += 1
                display.scroll(str(x_coord))
            elif button_a.was_pressed():
                get_x_coords = DONE
            
        get_y_coords = True
        while get_y_coords :
            if button_b.was_pressed():
                y_coord += 1
                display.scroll(str(y_coord))
            elif button_a.was_pressed():
                get_y_coords = DONE
     
    #For DEBUG show current coords
    curr_XY = str(x_coord)+ "," + str(y_coord)
    display.scroll(curr_XY)

    incoming = radio.receive()
    sleep(PAUSE)
    
    if incoming:
        mouse_coords = incoming.split(",")
        x_mouse = mouse_coords[0] #get mouse's x coord
        y_mouse = mouse_coords[1] #get mouse's y coord
        
        #calc distance to move in the x and y dirs
        x_steps = int(x_mouse) - x_coord
        y_steps = int(y_mouse) - y_coord
        
        #init new x,y directions and number of turns to execute
        new_xDir = ""
        new_yDir = ""
        num_turns = 0
        
        #determine whether to move EAST/WEST or stay the same
        if x_steps == 0:
            new_xDir = current_dir
        elif x_steps < 0 :
            new_xDir = "W"
        else:
            new_xDir = "E"
        
        #SEND x movement command with x_steps
        num_turns = calc_num_turns(current_dir, new_xDir)
        current_dir = new_xDir #update the direction we currently point in
        tell_robot(num_turns, x_steps) #move the robot (hopefully)
        
        #DEBUG
        display.scroll("xT: " + str(num_turns))
        sleep(500)
        display.scroll("dir: " + current_dir)
         
        if y_steps == 0:
            new_yDir = current_dir
        elif y_steps < 0 :
            new_yDir = "N"
        else:
            new_yDir = "S"
            
        #SEND y movement command with y_steps
        num_turns = calc_num_turns(current_dir, new_yDir)
        current_dir = new_yDir #update the direction we currently point in
        tell_robot(num_turns, y_steps)
        
        #DEBUG
        display.scroll("yT: " + str(num_turns))
        sleep(500)
        display.scroll("dir: " + current_dir)
        
        #update x_coord and y_coord to reflect our current position
        x_coord += x_steps
        y_coord += y_steps
        
    sleep(250)
