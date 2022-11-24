from  flask import Flask, render_template

web=Flask(__name__)

@web.route("/")
def Home():
    return render_template("index.html")

@web.route("/login")
def login():
    return render_template("login.html")

web.run()