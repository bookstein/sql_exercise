from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def get_student():
	hackbright_app.connect_to_DB()
	#request.args is a dictionary
	#.get() retrieves key's value if it is in dict
	#key is "student"
	student_github = request.args.get("student")
	return hackbright_app.get_student_by_github(student_github)


if __name__ == "__main__":
	app.run(debug=True)