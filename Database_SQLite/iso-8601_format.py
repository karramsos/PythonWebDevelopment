#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Dates(mdate text);
                      insert into dates values('2013-02-05');
                      insert into dates values('2012-10-13 12:33:12');
                      insert into dates values('13:23:04');
                      """)
    
    sql = "select datetime(mdate, '7 hours') from dates"
    cur.execute(sql)
    
    for r in cur.fetchall():
        print r[0]