import sys
import pendulo as PENDULO

param = sys.argv[1]

COMMAND = "light bulb {}".format(param)

PENDULO.Main.run(COMMAND)
