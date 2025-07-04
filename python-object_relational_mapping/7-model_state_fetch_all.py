#!/usr/bin/python3
""" Write a script that lists all State objects from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def get_state(username, password, database_name):
    # Connect to the database through the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database_name), echo=True)

    # Bind the engine to the session class and create a session instance
    session = sessionmaker(bind=engine)
    session = session()

    # Now we can query the database
    try:
        states = session.query(State).order_by(State.id)

        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()

if __name__ == "__main__":
    get_state(sys.argv[1], sys.argv[2], sys.argv[3])
