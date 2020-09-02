import config as CONFIG
import os

device = CONFIG.PENDULO.SERIAL_PORT
logs_path = CONFIG.PROJECT.LOGS_PATH

script = "sudo minicom -D {} -C tee {}/minicom.log >> /dev/null &".format(device, logs_path)

print(script)

os.system(script)
