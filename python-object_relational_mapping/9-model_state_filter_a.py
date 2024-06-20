#!/usr/bin/python3
"""
This script lists all State objects that
contain the letter 'a' from the database hbtn_0e_6_usa.
Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the `states` table, sorted in ascending order by `id`.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
