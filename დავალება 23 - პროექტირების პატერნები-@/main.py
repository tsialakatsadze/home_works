# from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello_world():
#     return "<h1> hello world </h1> <h2>hello world</h2"
# app.run(debug = True)

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def logo():
    return render_template("logo.html")
@app.route("/parallelogram")
def parallelogram():
    return render_template("parallelogram.html")
@app.route("/about_me")
def about_me():
    return render_template("about_me.html")
app.run(debug=True)