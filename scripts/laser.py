import sys
import pendulo as PENDULO

param = sys.argv[1]

COMMAND = "laser {}".format(param)

PENDULO.Main.run(COMMAND)
