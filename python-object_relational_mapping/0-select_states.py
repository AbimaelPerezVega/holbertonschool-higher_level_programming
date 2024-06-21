#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

from sys import argv
import MySQLdb  # type: ignore

if __name__ == "__main__":
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8",
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # Execute the SQL query to select all states
        # ordered by id in ascending order
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        states = cur.fetchall()

        # Print each state
        for state in states:
            print(state)

        # Close the cursor and the database connection
        cur.close()
        db.close()
    except MySQLdb.OperationalError as e:
        print(f"Error connecting to the database: {e}")
