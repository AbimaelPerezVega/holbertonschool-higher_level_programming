#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes three arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

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

    # Construct and execute the SQL query
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)

    # Fetch all the rows from the executed query
    cities = cur.fetchall()

    # Print each city in the required format
    for city in cities:
        print(city)

    # Close the cursor and the database connection
    cur.close()
    db.close()
