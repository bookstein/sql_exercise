from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def greet():
	return "Hello world"

@app.route("/EMILY")
def say_name():
	return "Your name is EMILY"

if __name__ == "__main__":
	app.run(debug=True)