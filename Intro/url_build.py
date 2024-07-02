import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route('/pass/<sname>/<int:marks>')
def passed(sname, marks):
    return f"<h1>Congrats {sname.title()}, You passed it with flying colors with {marks} marks!</h1>"

@app.route('/fail/<sname>/<int:marks>')
def failed(sname, marks):
    return f"<h1>{sname.title()}, this time luck wasn't with you but no worries, try again next year! Btw, you got {marks} marks.</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed", sname=name, marks=num))
    else:
        time.sleep(1)
        return redirect(url_for("passed", sname=name, marks=num))

if __name__ == "__main__":
    app.run(debug=True)
