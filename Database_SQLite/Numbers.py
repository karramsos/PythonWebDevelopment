#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.execute("create table Numbers(Id int, Cint integer, \
                CRea real)")
    cur.execute("insert into numbers values(1, 2, 2.3)")
    cur.execute("insert into numbers values(2, 8, 3.44)")
    cur.execute("insert into numbers values(3, 3, 1.0)")
    cur.execute("insert into numbers values(4, 12, 1.3)")
    cur.execute("insert into numbers values(5, 1, 7.7)")
    
    cur.execute("select sum(CInt) from numbers")
    row = cur.fetchone()
    print "The sum of integers is %d " % row[0]
    
    cur.execute("select sum(CRea) from numbers")
    row = cur.fetchone()
    print "The sum of reals is %f " % row[0]
    
    
