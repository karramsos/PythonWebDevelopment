#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.execute("CREATE TABLE Numbers(Id INT, CInt INTEGER, \
        CRea REAL)")
    cur.execute("INSERT INTO Numbers VALUES(1, 2, 2.3)")
    cur.execute("INSERT INTO Numbers VALUES(2, 8, 3.44)")
    cur.execute("INSERT INTO Numbers VALUES(3, 3, 1.0)")
    cur.execute("INSERT INTO Numbers VALUES(4, 12, 1.3)")
    cur.execute("INSERT INTO Numbers VALUES(5, 1, 7.7)")
    
    cur.execute("SELECT sum(CInt) FROM Numbers")
    row = cur.fetchone()
    print "The sum of integers is %d " % row[0]
    
    cur.execute("SELECT sum(CRea) FROM Numbers")
    row = cur.fetchone()
    print "The sum of reals is %f " % row[0]