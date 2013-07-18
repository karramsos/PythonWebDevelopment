#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')    

with con:
          
    cur = con.cursor() 
    cur.execute("CREATE TABLE Nums(Id INTEGER PRIMARY KEY)")
    cur.execute("INSERT INTO Nums VALUES(1)")
    cur.execute("INSERT INTO Nums VALUES(2.2)")

    cur.execute("SELECT Id FROM Nums")
    rows = cur.fetchmany(2)    

    for row in rows:
        print row[0]