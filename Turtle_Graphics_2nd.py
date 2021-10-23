from turtle import *
from functools import partial
bgpic("Colour_A_Turkey.gif") # change this to change the picture

#control the accuracy/speed of the drawing
step_size =8
pensize(4)
penup()

# whenever spacebar is pressed the current state  and next state switch values
current_state = penup
next_state = pendown
def space_bar():
    global current_state, next_state
    next_state()
    current_state, next_state = next_state, current_state
    #if the current stat is penup fill in with current colour
    if current_state == penup:
        end_fill()
    else:
        begin_fill()
onkey(space_bar, " ")

# undo do a mistake function
def mistake():
    undo()
onkey(mistake, "z")

#using partial function to store the following functions
#so they can be called  as arguments from a dictionary
#movement
strait = partial(fd, step_size)
reverse = partial(bk, step_size)
turn_rt = partial(rt, step_size)
turn_lf = partial(lt, step_size)

#colour
brow = partial(color, "brown")
gree = partial(color, "green")
yell = partial(color, "yellow")
oran = partial(color, "orange")
purp = partial(color, "purple")
red = partial(color, "red")
blue = partial(color, "blue")


#create a dictionary to store all the keys and there abilities
key_action = {"b" : blue, "r" : red, "p" : purp, "o" : oran,\
          "y" : yell, "g" : gree, "w" : brow, "Right" : turn_rt , "Up" : strait,\
          "Down" : reverse, "Left" : turn_lf, "z" : undo()}

#when a key in then above dictionary
#is pressed it's function  is activated
for pressed_key, activated_key in key_action.items():
    onkey(activated_key, pressed_key)

#make turtle look for key strokes with predefined function
listen()
#finish
done()