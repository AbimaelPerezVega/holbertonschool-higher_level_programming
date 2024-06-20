#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb 
import sys

def list_states(username, password, db_name):
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    # Fetch all the rows
    rows = cursor.fetchall()
    
    # Display the results
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
    else:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
