#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
of the database hbtn_0e_0_usa where the name matches the argument.

Arguments:
    mysql_username: Your MySQL username.
    mysql_password: Your MySQL password.
    database_name: The name of the database to connect to.
    state_name: The name of the state to search for.

The script connects to a MySQL server running on localhost at port 3306
and fetches all rows in the `states` table with the name matching the argument,
sorted in ascending order by `id`. It uses parameterized queries to prevent
SQL injection.
"""

if __name__ == "__main__":
    import sys
    import MySQLdb
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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
