#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.executescript("""
        CREATE TABLE Events(Id INT PRIMARY KEY, Desc TEXT, 
            Date INTEGER);
        INSERT INTO Events VALUES(1, 'Event 1', 1354687200);
        INSERT INTO Events VALUES(2, 'Event 2', 1336626000);
        INSERT INTO Events VALUES(3, 'Event 3', 1335826840);
        INSERT INTO Events VALUES(4, 'Event 4', 1333309115);
        """)
    
    cur.execute("""SELECT Desc, date(Date, 'unixepoch') 
        FROM Events""")
    
    for e in cur.fetchall():
        print e[0], "occurred at", e[1]
