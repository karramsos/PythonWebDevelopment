#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.execute("CREATE TABLE Ints(a INT, b INT)")
    cur.execute("INSERT INTO Ints VALUES(1, 2)")
    cur.execute("SELECT a / CAST(b AS REAL) FROM Ints")

    val = cur.fetchone()[0]

    print "The value is:", val