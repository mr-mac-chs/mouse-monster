# Add your Python code here. E.g.
from microbit import *
import radio

# turn the radio on
radio.on()

DONE = False
x_coords_done = False
x_coord = 0
y_coord = 0

display.scroll('TX!')
sleep(2000)
display.clear()

while True:
    #display.scroll('TX!')
    #sleep(250)
    
    if button_a.was_pressed():
        x_coord = -1
        y_coord = -1
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
     
     
    tx_string = str(x_coord)+ "," + str(y_coord)
    #display.scroll(tx_string,wait=False)
    
    #Need to sit and listen
    #sleep(2000)
    
    if accelerometer.was_gesture("shake"):
        display.clear()
        sleep(250)
        display.scroll(tx_string)
        radio.send(tx_string)
        sleep(1000)
