import sys
import pendulo as PENDULO
import time

deltaX = sys.argv[1]
N = sys.argv[2]

COMMAND = "cfg\t{}\t{}".format(deltaX, N)
START_COMMAND = "str"

PENDULO.Main.run(COMMAND)
time.sleep(15)
PENDULO.Main.run(START_COMMAND)
