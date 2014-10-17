"""This is a practice version of hackbright_app.py
created from scratch without looking at the starter code provided in the exercise. The app must connect to the database and run functions with queries of various kinds.
Can ignore the command-line if-else statements of the original assignment."""

import sqlite3

#must use global names for database and connection - accessed by all funcs
c = None
CONN = None

#connect to database with sqlite3 (must import)
def connect_to_DB():
	# 'global' keyword allows you to change global vars from local context
	global c, CONN
	# Create a Connection object that represents the database
	CONN = sqlite3.connect("hackbright.db")
	# create a cursor object
	c = CONN.cursor()

def get_student_by_github(github):
	query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
	c.execute(query, (github,))
	row = c.fetchone()
	print "Student: ", row

def add_student(first_name, last_name, github):
	query = """INSERT INTO Students VALUES (?,?,?)"""
	validate = raw_input("You're sure? (y/n)")
	if validate == "y":
		c.execute(query, (first_name, last_name, github))
		print "Added %s %s, github %s" % (first_name, last_name, github)
		CONN.commit()

def get_project_by_title(title):
	query = """SELECT * FROM Projects WHERE title = ?"""
	c.execute(query, (title,))
	row = c.fetchone()
	# print row
	print "About this project:"
	print "Project: %s, description: %s, max grade: %d" % (row[1], row[2], row[3])

def add_project(title, description, max_grade):
	query = """INSERT INTO Projects (title, description, max_grade) VALUES (?, ?, ?)"""
	validate = raw_input("You're sure? (y/n)")
	if validate == "y":
		c.execute(query, (title, description, max_grade))
		print "Successfully added %s, %s, max grade %d" % (title, description, int(max_grade))
		CONN.commit()

def get_student_grade_by_project(first_name, last_name, project_title):
	query = """SELECT first_name, last_name, project_title, grade
	FROM GradesView WHERE first_name = ? AND last_name = ? AND project_title = ?"""
	c.execute(query, (first_name, last_name, project_title))
	row = c.fetchone()
	print row

def give_grade(github, project_title, grade):
	query = """INSERT INTO Grades (student_github, project_title, grade) VALUES (?, ?, ?)"""
	validate = raw_input("You're sure? (y/n)")
	if validate == "y":
		c.execute(query, (github, project_title, grade))
		print "Successfully added project %s, grade %s, to %s" % (project_title, grade, github)
		CONN.commit()


def main():
	connect_to_DB()
	command = None

	#continue to ask for raw_input as long as command is not quit
	while command != quit:
		cmd_line_args = raw_input("Look in database>> ")
		cmd_line_args = cmd_line_args.split(",")
		for arg in cmd_line_args:
			arg = arg.strip()
		command = cmd_line_args[0]
		args = cmd_line_args[1:]

		if command == "get_student":
			get_student_by_github(*args)
		elif command == "add_student":
			add_student(*args)
		elif command == "get_project":
			get_project_by_title(*args)
		elif command == "add_project":
			add_project(*args)
		elif command == "get_grade":
			get_student_grade_by_project(*args)
		elif command == "give_grade":
			give_grade(*args)
		elif command == quit:
			break

	CONN.close()





if __name__ == "__main__":
	main()