from flask import Flask, redirect, url_for, render_template
import pathlib


app = Flask(__name__)
current_path = pathlib.Path(__file__).resolve()
print(current_path)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/<name>/")
def user(name):
    return render_template("index.html", contents = ['big joe', 'hello', 'jack'])


@app.route("/admin/")
def admin():
    return render_template("admin.html")


if __name__ == "__main__":
    app.run(debug=True)