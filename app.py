from flask import Flask, make_response, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    saved_name = request.cookies.get("saved_name")
    return render_template("index.html")

@app.route("/new_cookie")
def new_cookie():
    response = make_response("Hello world!")
    response.set_cookie("mycookie", "myvalue")

    return response

@app.route("/show_cookie")
def show_cookie():
    cookie_value = request.cookies.get("mycookie")

    return cookie_value

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9999)