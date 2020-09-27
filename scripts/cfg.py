import sys
import pendulo as PENDULO

deltaX = sys.argv[1]
N = sys.argv[2]

COMMAND = "cfg\t{}\t{}".format(deltaX, N)

PENDULO.Main.run(COMMAND)
