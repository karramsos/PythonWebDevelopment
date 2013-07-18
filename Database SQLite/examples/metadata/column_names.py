#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute('PRAGMA table_info(Cars)')
    
    data = cur.fetchall()
    
    for d in data:
        print d[0], d[1], d[2]