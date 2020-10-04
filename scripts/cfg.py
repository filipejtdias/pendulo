import sys
import pendulo as PENDULO
import time

deltaX = sys.argv[1]
N = sys.argv[2]

CONFIG_COMMAND = "cfg\t{}\t{}".format(deltaX, N)
START_COMMAND = "str"

COMMAND = "{}\r{}".format(CONFIG_COMMAND, START_COMMAND)

PENDULO.Main.run(COMMAND)
