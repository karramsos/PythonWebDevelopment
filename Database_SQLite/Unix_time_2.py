#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    cur.executescript("""
                      create table Events2(Id int primary key, Desc text, Date integer);
                      insert into events2 values(1, 'Event 1', 1354687200);
                      insert into events2 values(2, 'Event 2', 1336626000);
                      insert into events2 values(3, 'Event 3', 1335826840);
                      insert into events2 values(4, 'Event 4', 1333309115);
                      """)
    
    cur.execute("""select Desc, date(Date, 'unixepoch') from events2""")
    
    for e in cur.fetchall():
        print e[0], "occured at", e[1]
    