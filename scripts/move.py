import sys
import pendulo as PENDULO

def action_from(argument): 
    switcher = { 
        "0": "forward", 
        "1": "backward",
        "2": "to photodiode"
    } 
  
    return switcher.get(argument, "NaN")

_direction = sys.argv[1]
direction = action_from(_direction)

deltaX = sys.argv[2]
speed = sys.argv[3]
acceleration = sys.argv[4]

COMMAND = "move {} {} {} {}".format(direction, deltaX, speed, acceleration)

PENDULO.Main.run(COMMAND)
