#!/usr/bin/python3
""" Write a script that lists all State objects from the database
"""
import sys
from model_state import Base, State

def get_state(username, password, database_name):
    State.__tablename__

if __name__ == "__main__":
    get_state(sys.argv[1], sys.argv[2], sys.argv[3])