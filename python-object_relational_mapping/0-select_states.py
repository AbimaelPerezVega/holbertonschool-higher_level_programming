#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

def main():
    """
    Connects to a MySQL database and lists all states in ascending order by id.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password, db=database_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all the rows from the executed query
        rows = cursor.fetchall()

        # Print each row
        for row in rows:
            print(row)

        # Close the cursor and database connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    main()
