import sys
import pendulo as PENDULO

direction = sys.argv[1] # forward|backward|to photodiode
deltaX = sys.argv[2]
speed = sys.argv[3]
acceleration = sys.argv[4]

COMMAND = "move " + direction + " " + deltaX + " " + speed + " " + acceleration + "\r"

PENDULO.Main.run(COMMAND)
