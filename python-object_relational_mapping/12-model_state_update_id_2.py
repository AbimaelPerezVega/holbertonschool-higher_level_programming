#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query the State object with id=2
    state_to_update = session.query(State).filter(State.id == 2).one_or_none()

    if state_to_update is not None:
        # Change the state's name to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
