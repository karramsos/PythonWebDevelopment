#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')
con.isolation_level = None

cur = con.cursor()

with con:
    cur.execute("drop table if exists Friends")
    cur.execute('''create table Friends(Id integer primary key, Name text)''')
    
try:
    cur.execute("insert into friends(name) values('Tom')")
    cur.execute("insert into friends(name) values('Rebecca')")
    
    with con:
        cur.execute("insert into friends(name) values('Jim')")
        cur.execute("insert into friends(name) values('Robert')")
        raise Exception
        
except:
    
    print "There was an error"
    
for row in cur.execute("select * from friends"):
    print row
