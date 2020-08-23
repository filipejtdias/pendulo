import sys
import pendulo as PENDULO

param = sys.argv[1]
COMMAND = "light bulb " + param + "\r"

PENDULO.Main.run(COMMAND)
