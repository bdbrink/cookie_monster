from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/new_cookie")
def new_cookie():
    response = make_response("Hello world!")