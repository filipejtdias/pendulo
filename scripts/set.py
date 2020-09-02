import sys
import pendulo as PENDULO

def action_from(argument): 
    switcher = { 
        "0": "maximum position", 
        "1": "sphere diameter",
        "2": "pendulum length",
        "3": "origin position",
        "4": "vertical position",
        "5": "photodiode position",
        "6": "pulley diameter",
        "7": "ID string"
    } 
  
    return switcher.get(argument, "NaN")

param = sys.argv[1]
option = action_from(param)
value = sys.argv[2]

COMMAND = "set {} {}".format(option, value)

PENDULO.Main.run(COMMAND)
