#!/usr/bin/python3
""" module that contains state my get"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{\
}'.format(sys.argv[1],
          sys.argv[2],
          sys.argv[3],
          sys.argv[4]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker()
    session = session(bind=engine)
    state = session.query(State).filter(State.name.like(sys.argv[4]))
    if state.count() == 0:
        print("Not found")
    for hell in state:
        print(hell.id)
        exit()
