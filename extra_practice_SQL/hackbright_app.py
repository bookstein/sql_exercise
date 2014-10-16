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
	print "success!", row


def main():
	connect_to_DB()
	command = None

	#continue to ask for raw_input as long as command is not quit
	while command != quit:
		cmd_line_args = raw_input("Look in database>> ")
		cmd_line_args = cmd_line_args.strip().split(",")
		command = cmd_line_args[0]
		args = cmd_line_args[1:]

		if command == "get_student":
			get_student_by_github(*args)
		elif command == quit:
			break

	CONN.close()





if __name__ == "__main__":
	main()