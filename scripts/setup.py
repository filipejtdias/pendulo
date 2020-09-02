import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import config as CONFIG

config_file = CONFIG.PENDULO.SETUP_FILENAME

COMMAND = "sudo picpgm -p_code {} && sudo picpgm -p_cfg {}".format(config_file, config_file)

print("--DEBUG--\n{}".format(COMMAND))
# os.system(COMMAND)
