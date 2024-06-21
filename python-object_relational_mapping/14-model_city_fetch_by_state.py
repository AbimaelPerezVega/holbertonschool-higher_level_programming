#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

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

    # Query all City objects and join with State objects to get the state name
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
