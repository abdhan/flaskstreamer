from flask import Flask, redirect, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return("hello world")

@app.route('/cam')
def cam():
    return(render_template("cam.html"))

if __name__ == '__main__':
    app.run()
