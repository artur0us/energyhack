import logging, threading, os, signal, json
from flask import Flask, render_template, Response, request, redirect

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Global variables
serverThread = None
serverApp = Flask(__name__, static_folder="web", static_url_path="", template_folder="web")

# Server's answer actions
# -- Page routes
@serverApp.route("/")
def ws_indexPage():
	return render_template("index.html")

@serverApp.route("/admin")
def ws_adminPage():
	return render_template("admin.html")

# -- API routes
@serverApp.route("/api/checkAuth")
def ws_checkAuth():
	if localAPI_checkAuth(request.args.get("login"), request.args.get("password")):
		return "ok"
	else:
		return "error"

@serverApp.route("/api/getInfo")
def ws_getInfo():
	if localAPI_checkAuth(request.args.get("login"), request.args.get("password")):
		accountDatabase = json.load(open("db/accounts.json"))["Users"]
		for i in range(0, len(accountDatabase)):
			if accountDatabase[i][0] == request.args.get("login"):
				return json.dumps([accountDatabase[i][2], json.load(open("db/balance.json"))])
	else:
		return "error"

def localAPI_checkAuth(myLogin, myPassword):
	accountDatabase = json.load(open("db/accounts.json"))["Users"]
	for i in range(0, len(accountDatabase)):
		if accountDatabase[i][0] == myLogin:
			if accountDatabase[i][1] == myPassword:
				return True
	return False

def startWebServer():
	print("[i] Starting web server...")
	serverApp.run("0.0.0.0", 9000, debug=True)

def startAllThreads():
	"""global serverThread
	serverThread = threading.Thread(target = startWebServer, name = "myServerThread")
	serverThread.start()"""
	startWebServer()

# Main actions...

def Main():
	startAllThreads()

Main()