import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Home Page!</h1>"

@app.route('/pass')
def passed():
    return "<h1>Congrats! You passed it with flying colors!</h1>"

@app.route('/fail')
def failed():
    return "<h1>This time luck wasn't with you but no worries, try again next year!!</h1>"

@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else:
        time.sleep(1 )
        return redirect(url_for("passed"))

if __name__ == "__main__":
    app.run(debug=True)
