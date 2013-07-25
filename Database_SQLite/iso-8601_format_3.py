#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import datetime

con = lite.connect(':memory:')

d1 = datetime.datetime(2013, 1, 1, 15, 12, 0).isoformat()
d2 = datetime.datetime.fromtimestamp(1360350273).isoformat()
d3 = datetime.datetime.now().isoformat()
d4 = datetime.datetime.utcnow().isoformat()

with con:
    
    cur = con.cursor()
    
    cur.execute("create table Dates3(mdate text)")
    cur.execute("insert into dates3 values(?)", (d1, ))
    cur.execute("insert into dates3 values(?)", (d2, ))
    cur.execute("insert into dates3 values(?)", (d3, ))
    cur.execute("insert into dates3 values(?)", (d4, ))
    
    cur.execute("select mdate from dates3")
    
    for r in cur.fetchall():
        print r[0]
    