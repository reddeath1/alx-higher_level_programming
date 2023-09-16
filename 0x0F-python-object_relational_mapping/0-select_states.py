#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
    cur = db.cursor()
    rows = cur.execute('SELECT * FROM states ORDER BY states.id;')
    data = cur.fetchall()
    for row in data:
        print(row)
    cur.close()
    db.close()
