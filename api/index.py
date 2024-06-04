from flask import Flask, render_template

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test_endpoint():
    return "Hello, this is a test endpoint!", 200


@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")
