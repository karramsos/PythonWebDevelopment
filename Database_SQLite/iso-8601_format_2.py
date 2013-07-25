#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Dates2(mdate text);
                      insert into Dates2 values('2013-02-05');
                      insert into dates2 values('2012-10-13');
                      insert into dates2 values('2012-05-11');
                      insert into dates2 values('2012-11-01');
                      insert into dates2 values('2013-01-26');
                      """)
    
    cur.execute("select min(mdate) from dates2")
    r = cur.fetchone()[0]
    print r
    
    print "**********************"
    
    cur.execute("select max(mdate) from dates2")
    r = cur.fetchone()[0]
    print r
    
    print "**********************"
    
    cur.execute("select mdate from dates2 order by mdate")
    
    for r in cur.fetchall():
        print r[0]
    
