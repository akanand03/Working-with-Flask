from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>Welcome to the Home Page!</h1>"


@app.route("/about")
def about():
	return "<h1>Welcome to the About Page!</h1>"

@app.route("/welcome/<name>")
def welcome (name):
	return f"<h1>Welcome {name}!</h1>"


# Running our first flask app 
if __name__ == '__main__':
	app.run(debug=True)

