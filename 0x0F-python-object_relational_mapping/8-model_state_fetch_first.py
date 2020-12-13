
#!/usr/bin/python3
''' lists all states from database'''


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(State).order_by(State.id).first()
    if st:
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()
