#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    cur.execute("create table Nums2(Id integer primary key)")
    cur.execute("insert into nums2 values(1)")
    cur.execute("insert into nums2 values(2.2)")
    
    cur.execute("select Id from nums2")
    rows = cur.fetchmany(2)
    
    for row in rows:
        print row[0]