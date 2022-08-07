import email
from flask import Flask, request, send_file, session, redirect, Response, jsonify
from flask_cors import CORS, cross_origin
from flask_session import Session


import database
from config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
CORS(app, supports_credentials=True)
server_session = Session(app)
db = database.Database()

UPLOAD_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/signup", methods = ['POST'])
def signup():
    data = request.get_json()
    username = data["username"]
    password = data["username"]
    email = data["email"]
    if db.is_valid_username(username):
        db.signup(username, password, email)
        return Response(status=201)
    return Response("Account already exists", status=409)


@app.route("/login", methods = ['POST'])
#@cross_origin(origin='*',headers=['Control-Allow-Credentials','Access-Control-Allow-Origin'])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["username"]
    if db.login(username, password):
        session['user'] = username
        return Response(status=200)
    return Response("Invalid username or password", status=400)


@app.route("/logout", methods = ['GET'])
def logout():
    session.pop("user")
    return Response(status=200)


@app.route("/@me", methods = ['GET'])
def verf():
    user = session.get("user")
    if user:
        return Response(jsonify(status="true"), status=200)
    return Response(jsonify(status="false"), status=401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)