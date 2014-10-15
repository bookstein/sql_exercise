from flask import Flask, request, render_template
import hackbright_app

app = Flask(__name__)

@app.route("/student")
def get_student():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    grades = hackbright_app.get_student_grades(row[0], row[1])
    html = render_template("student_info.html", first_name=row[0], last_name=row[1], github=row[2], 
        rows = grades)
    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")

@app.route("/project")
def get_project():
    hackbright_app.connect_to_db()
    project = request.args.get("project")
    description = hackbright_app.get_projects(project)
    rows = hackbright_app.get_all_grades_for_project(project)
    html = render_template("project_grades.html", rows=rows, title=description[1], descrip=description[2],
        max_grade= description[3])
    return html



if __name__ == "__main__":
    app.run(debug=True)