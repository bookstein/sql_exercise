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

@app.route("/project")
def get_project():
	hackbright_app.connect_to_DB()
	# get value of project from URL (which was set in student_info link)
	project_title = request.args.get("project")
	# get project info using get_project()
	project_row = hackbright_app.get_project_by_title(project_title)
	# get all student grades on this project using get_student_grade_by_project()
	grades_rows = hackbright_app.get_all_project_grades(project_title)
	html = render_template("projects.html", project_title = project_row[1],
		description = project_row[2], max_grade = project_row[3],
		grades_rows = grades_rows)
	return html

if __name__ == "__main__":
	app.run(debug=True)