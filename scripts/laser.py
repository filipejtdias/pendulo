import sys
import pendulo as PENDULO

param = sys.argv[1]
COMMAND = "laser " + param + "\r"

PENDULO.Main.run(COMMAND)
