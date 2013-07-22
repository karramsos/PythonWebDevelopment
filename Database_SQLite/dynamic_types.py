#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    cur.execute("create table Nums(Id int, Val int)")
    cur.execute("insert into nums values(1, 1.2)")
    cur.execute("insert into nums values(2, 'Book')")
    
    cur.execute("select Id, Val from Nums")
    rows = cur.fetchmany(2)
    
    for row in rows:
        print row[0], row[1]