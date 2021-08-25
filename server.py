#!/usr/bin/python3


from datamanager import DataManager
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

dataManager = DataManager()


@app.route("/", methods= ["GET"])
def home():
	return "{name:test}"
	

@app.route('/get/on_off/', methods=['GET'])
def get_on_off():
	global dataManager
	return '1' if dataManager.currOnOff else '0', 200


@app.route('/set/on_off/<arg>', methods=['POST'])
def set_on_off(arg):
	#print("argomento     ", str(arg))
	global dataManager
	dataManager.setOnOff(arg)
	
	return '', 204


@app.route('/get/brightness/', methods=['GET'])
def get_brightness():
    global dataManager
    #print('get brightness')
    return str(dataManager.currLevel), 200


@app.route('/set/brightness/<int:arg>', methods=['POST'])
def set_brightness(arg):
	global dataManager
	dataManager.setLevel(arg)
	#print('set brightness:', arg)
	return '', 204

    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
	
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def startServer():
	app.run(host='0.0.0.0', port=5000)