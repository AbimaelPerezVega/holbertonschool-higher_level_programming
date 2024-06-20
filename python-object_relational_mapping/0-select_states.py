#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb  # type: ignore
import sys
# from sqlalchemy import create_engine, Column, Integer, String # type: ignore
# from sqlalchemy.orm import declarative_base, sessionmaker # type: ignore


def main():
    """
    Connects to a MySQL database and lists all states in ascending order by id.
    """
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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


if __name__ == "__main__":
    main()
