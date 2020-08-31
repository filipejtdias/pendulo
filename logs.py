import config as CONFIG
import os

def start():
	device = CONFIG.PENDULO.SERIAL_PORT
	script = "sudo minicom -D {} -C tee ~/pendulo/logs/minicom.log >> /dev/null &".format(device)
	run(script)

def run(script):
	os.system(script)

start