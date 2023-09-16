#!/usr/bin/python3
"""
@author: Frank Galos
"""
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    dbn = args[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, dbn))
    # create session object class from database engine
    Session = sessionmaker(bind=engine)
    # create instance of new session class
    session = Session()
    results = session.query(State.name, City.id, City.name)\
                     .join(City, City.state_id == State.id)\
                     .order_by(City.id)
    for result in results:
        print("{}: ({}) {}".format(result[0], result[1], result[2]))
