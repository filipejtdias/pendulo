import sys
import pendulo as PENDULO

speed = sys.argv[1]
acceleration = sys.argv[2]

COMMAND = "go to origin {} {}".format(speed, acceleration)

PENDULO.Main.run(COMMAND)
