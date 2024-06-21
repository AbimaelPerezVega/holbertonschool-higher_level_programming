#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state using the database hbtn_0e_4_usa.
The script is safe from SQL injection.
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

    # Construct and execute the SQL query (safe from SQL injection)
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cur.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    cities = cur.fetchall()

    # Print each city, joined by a comma
    print(", ".join(city[0] for city in cities))

    # Close the cursor and the database connection
    cur.close()
    db.close()
