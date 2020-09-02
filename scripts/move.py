import sys
import pendulo as PENDULO

_direction = sys.argv[1]

direction = ""
if _direction == "0": # forward
	direction = "forward"
elif _direction == "1": # backward
	direction = "backward"
elif _direction == "2": # to photodiode
	direction = "'to photodiode'"

deltaX = sys.argv[2]
speed = sys.argv[3]
acceleration = sys.argv[4]

COMMAND = "move {} {} {} {}".format(direction, deltaX, speed, acceleration)

PENDULO.Main.run(COMMAND)
