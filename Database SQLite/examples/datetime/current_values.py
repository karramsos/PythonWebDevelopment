#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import time

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.executescript("""
        CREATE TABLE Events(Id INT PRIMARY KEY, Desc TEXT, 
            timestamp NOT NULL DEFAULT current_timestamp);
        INSERT INTO Events(Id, Desc) VALUES(1, 'Event-1');
        """)
    
    time.sleep(2)
    sql = "INSERT INTO Events(Id, Desc) VALUES(2, 'Event-2')"
    cur.execute(sql)
    time.sleep(3)
    sql = "INSERT INTO Events(Id, Desc) VALUES(3, 'Event-3')"
    cur.execute(sql)
    time.sleep(4)
    sql = "INSERT INTO Events(Id, Desc) VALUES(4, 'Event-4')"
    cur.execute(sql)
            
    sql = "SELECT * from Events"
    cur.execute(sql)
    
    for f1, f2, f3 in cur.fetchall():
        print f1, f2, f3
        
        
    

