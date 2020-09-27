import config as CONFIG
import os
import time
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    server = CONFIG.SERVER.PUBLIC_IP
    cam_port = CONFIG.PENDULO.CAM_PORT
    cam_url = "http://{}:{}/".format(server, cam_port)
    return render_template('index.html', cam_url=cam_url)

@app.route('/setup', methods=['GET'])
def setup():
        
    script_file="setup.py"
    run(script_file)
    return index()

@app.route('/light', methods=['GET'])
def light():
    
    action = request.args.get('action')
    
    script_file="light.py {}".format(action)
    run(script_file)
    return index()

@app.route('/laser', methods=['GET'])
def laser():
    
    action = request.args.get('action')
    
    script_file="laser.py {}".format(action)
    run(script_file)
    return index()

@app.route('/set', methods=['GET'])
def set():
    
    action = request.args.get('action')
    value = request.args.get('value')
    
    script_file="set.py {} {}".format(action, value)
    run(script_file)
    return index()

@app.route('/move', methods=['GET'])
def move():

    direction = request.args.get('direction')
    deltaX = request.args.get('deltaX')
    speed = request.args.get('speed')
    acceleration = request.args.get('acceleration')
    
    script_file="move.py {} {} {} {}".format(direction, deltaX, speed, acceleration)
    run(script_file)
    return index()

@app.route('/cfg', methods=['GET'])
def cfg():

    deltaX = request.args.get('deltaX')
    N = request.args.get('n')
    
    script_file="cfg.py {} {}".format(deltaX, N)
    run(script_file)
    return index()

@app.route('/stream')
def stream():

    logs_path = CONFIG.PROJECT.LOGS_PATH

    file = '{}/minicom.log'.format(logs_path)

    def generate():
        with open(file) as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype='text/plain')

def run(script_file):

    script_path = CONFIG.PROJECT.SCRIPTS_PATH

    script = "python {}/{}".format(script_path, script_file)

    app.logger.debug(script)
    os.system(script)

if __name__ == '__main__':
    host = CONFIG.SERVER.HOST
    port = CONFIG.SERVER.PORT
    app.run(debug=True, host=host, port=port)
