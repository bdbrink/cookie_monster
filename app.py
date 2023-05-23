from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/new_cookie")
def new_cookie():
    response = make_response("Hello world!")
    response.set_cookie("mycookie", "myvalue")

    return response

@app.route("/show_cookie")
def show_cookie():
    cookie_value = request.cookies.get("mycookie")

    return cookie_value

