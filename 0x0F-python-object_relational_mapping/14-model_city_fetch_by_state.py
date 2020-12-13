#!/usr/bin/python3
"""module that contains city fetech"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}\
@localhost/{}'.format(sys.argv[1],
                      sys.argv[2],
                      sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session = session(bind=engine)
    for s, c in session.query(City, State).filter(City.state_id.like(
            State.id)):
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
