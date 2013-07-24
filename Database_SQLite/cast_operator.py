#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.execute("create table Ints(a INT, b INT)")
    cur.execute("insert into Ints values(1, 2)")
    cur.execute("select a / CAST(b AS REAL) from Ints")
    
    val = cur.fetchone()[0]
    
    print "The value is:", val