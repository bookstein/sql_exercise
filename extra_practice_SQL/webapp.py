from flask import Flask, render_template, request
import hackbright_app

app = Flask(__name__)

@app.route("/")
def show_home():
	date = "10/17/14"
	html = render_template("home.html", date = date)
	return html

@app.route("/student")
def get_student():
	hackbright_app.connect_to_DB()
	#request.args is a dictionary
	#.get() retrieves key's value if it is in dict
	#key is "student"
	student_github = request.args.get("github")
	student_row = hackbright_app.get_student_by_github(student_github)
	grade_rows = hackbright_app.get_all_grades(student_row[0], student_row[1])
	html = render_template("student_info.html", first_name = student_row[0],
		last_name = student_row[1], github = student_row[2],
		grade_rows = grade_rows)
	return html

if __name__ == "__main__":
	app.run(debug=True)