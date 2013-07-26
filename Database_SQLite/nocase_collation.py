#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Words3(Word text collate nocase);
                      insert into words3 values('elite');
                      insert into words3 values('frost');
                      insert into words3 values('alpha');
                      insert into words3 values('Albert');
                      insert into words3 values('car');
                      insert into words3 values('dolphin');
                      insert into words3 values('Dublin');
                      insert into words3 values('bus');
                      insert into words3 values('ghost');
                      """)
    
    sql = "select word from words3 order by word asc"
    cur.execute(sql)
    
    for r in cur.fetchall():
        print r[0]
    