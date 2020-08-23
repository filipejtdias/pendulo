import config as CONFIG
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/light', methods=['GET'])
def light():
	
	action = request.args.get('action')
	
	script="python scripts/light.py {}".format(action)
	run(script)
	return index()

@app.route('/move', methods=['GET'])
def move():

	direction = request.args.get('direction')
	deltaX = request.args.get('deltaX')
	speed = request.args.get('speed')
	acceleration = request.args.get('acceleration')

	_direction = ""
	if direction == "0": # forward
		_direction = "forward"
	elif direction == "1": # backward
		_direction = "backward"
	elif direction == "2": # to photodiode
		_direction = "'to photodiode'"
	else:
		app.logger.error(direction)
	
	script="python scripts/move.py {} {} {} {}".format(_direction, deltaX, speed, acceleration)
	run(script)
	return index()

def run(script):
	app.logger.debug(script)
	os.system(script)

if __name__ == '__main__':
	host = CONFIG.SERVER.HOST
	port = CONFIG.SERVER.PORT
	app.run(debug=True, host=host, port=port)
