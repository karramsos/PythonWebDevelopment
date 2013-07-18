#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')    

with con:
          
    cur = con.cursor() 
    cur.execute("CREATE TABLE Nums(Id INT, Val INT)")
    cur.execute("INSERT INTO Nums VALUES(1, 1.2)")
    cur.execute("INSERT INTO Nums VALUES(2, 'Book')")

    cur.execute("SELECT Id, Val FROM Nums")
    rows = cur.fetchmany(2)    

    for row in rows:
        print row[0], row[1]