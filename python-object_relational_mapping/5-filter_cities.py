#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for its cities.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the `cities` table for a given state,
sorted in ascending order by `cities.id`.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
