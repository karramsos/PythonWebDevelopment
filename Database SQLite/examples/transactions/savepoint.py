#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('test.db')
con.isolation_level=None

try:

    con.execute("BEGIN TRANSACTION")
    con.execute("DROP TABLE IF EXISTS Ints")
    con.execute("CREATE TABLE Ints(i INT)")
    con.execute("INSERT INTO Ints VALUES(1)")
    con.execute("SAVEPOINT sp1")
    con.execute("INSERT INTO Ints VALUES(2)")
    con.execute("SAVEPOINT sp2")
    con.execute("INSERT INTO Ints VALUES(5)")
    con.execute("ROLLBACK TRANSACTION TO sp2")
    con.execute("RELEASE sp1")
    #con.execute("RELEASE sp2")
    con.execute("COMMIT")  
    
except lite.Error, e:
    
    if con:
        con.rollback()
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:    
    
    if con:
        con.close() 