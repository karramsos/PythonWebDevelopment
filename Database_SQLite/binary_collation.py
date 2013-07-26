#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Words(Word text);
                      insert into words values('elite');
                      insert into words values('frost');
                      insert into words values('alpha');
                      insert into words values('car');
                      insert into words values('dolphin');
                      insert into words values('bus');
                      insert into words values('ghost');
                      """)
    
    sql = "select word from words order by word asc"
    cur.execute(sql)
    
    for r in cur.fetchall():
        print r[0]
    