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

@app.route('/light/<action>', methods=['POST'])
def light(action):
    
    script_file="light.py {}".format(action)
    run(script_file)
    return index()

@app.route('/laser/<action>', methods=['POST'])
def laser(action):
    
    script_file="laser.py {}".format(action)
    run(script_file)
    return index()

@app.route('/move', methods=['POST'])
def move():

    direction = request.form['direction']
    deltaX = request.form['deltaX']
    speed = request.form['speed']
    acceleration = request.form['acceleration']
    
    script_file="move.py {} {} {} {}".format(direction, deltaX, speed, acceleration)
    run(script_file)
    return index()

@app.route('/origin', methods=['POST'])
def origin():
    
    speed = request.form['speed']
    acceleration = request.form['acceleration']
    
    script_file="origin.py {} {}".format(speed, acceleration)
    run(script_file)
    return index()

@app.route('/set', methods=['POST'])
def set():
    
    action = request.form['action']
    value = request.form['value']
    
    script_file="set.py {} {}".format(action, value)
    run(script_file)
    return index()

@app.route('/cfg', methods=['POST'])
def cfg():

    deltaX = request.form['deltaX']
    N = request.form['n']
    
    script_file="cfg.py {} {}".format(deltaX, N)
    run(script_file)
    return index()

@app.route('/setup', methods=['POST'])
def setup():
        
    script_file="setup.py"
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
