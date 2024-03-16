from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from math import *



@app.route('/')
def index():
        return render_template("index.html")



@app.route('/result', methods=["POST"])
def result():
        a = request.form.get("a")
        b = request.form.get("b")
        a = int(a)
        b = int(b)
        c = sqrt((a * a) + (b * b))
        return render_template("result.html", c=c)
