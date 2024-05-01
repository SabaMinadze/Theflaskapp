from flask import Flask, render_template, request, redirect
app = Flask(__name__)
from math import *



@app.route('/')
def index():
        return render_template("index.html")



@app.route('/result', methods=["POST"])
def result():
        if request.method == "POST":
                a = request.form.get("a")
                b = request.form.get("b")
                a = int(a)
                b = int(b)
                c = sqrt((a * a) + (b * b))
                return render_template("result.html", c=c)



@app.route('/heron', methods=["POST"])
def heron():
        if request.method == "POST":        
                a1 = request.form.get("a1")
                b1 = request.form.get("b1")
                c1 = request.form.get("c1")
                a1 = int(a1)
                b1 = int(b1)
                c1 = int(c1)
                p1 = ((a1 + b1 + c1) / 2)
                p1 = int(p1)
                answ = sqrt(p1 * (p1 - a1) * (p1 - b1) * (p1 - c1))
                return render_template("heron.html", answ=answ)
        

      


if __name__ == '__main__':
        app.run(debug=True)
