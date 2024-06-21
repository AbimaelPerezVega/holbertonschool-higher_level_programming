#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, using format to
create the SQL query with user input.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Construct the SQL query using format with user input
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(state_name)
    )

    # Execute the SQL query
    cur.execute(query)

    # Fetch all the rows from the executed query
    states = cur.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cur.close()
    db.close()
