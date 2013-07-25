#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import time

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Events(Id int primary key, Desc text, timestamp not null default current_timestamp);
                      insert into events(Id, desc) values(1, 'Event-1');
                      """)
    
    time.sleep(2)
    sql = "insert into events(Id, Desc) values(2, 'Event-2')"
    cur.execute(sql)
    time.sleep(3)
    sql = "insert into events(Id, Desc) values(3, 'Event-3')"
    cur.execute(sql)
    time.sleep(4)
    sql = "insert into events(Id, Desc) values(4, 'Event-4')"
    cur.execute(sql)
    
    sql = "select * from events"
    cur.execute(sql)
    
    for f1, f2, f3 in cur.fetchall():
        print f1, f2, f3
    