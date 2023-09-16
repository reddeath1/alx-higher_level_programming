#!/usr/bin/python3
"""
@author: Frank Galos
"""
import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: {} username password database name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    dbn = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=dbn, port=3306)
    cursor = db.cursor()
    num_rows = cursor.execute("SELECT cities.id, cities.name, states.name\
                           FROM cities INNER JOIN states\
                           ON cities.state_id=states.id\
                           ORDER BY cities.id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
