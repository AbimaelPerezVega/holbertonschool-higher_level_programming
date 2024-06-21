#!/usr/bin/python3
"""Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Create a database engine
    db_string = 'mysql+mysqldb://{}:{}@localhost/{}'\
        .format(username, password, dbname)
    engine = create_engine(db_string, pool_pre_ping=True)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query State object by state_name
    result = session.query(State)\
                    .filter(State.name == state_name)\
                    .first()

    # Check if result is None
    if result:
        print(result.id)
    else:
        print("Not found")

    # Close the session
    session.close()
