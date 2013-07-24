#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    con.row_factory = lite.Row
    
    cur = con.cursor()
    cur.execute('select * from cars')
    
    rows = cur.fetchall()
    
    for row in rows:
        print row['Id'], row['name'], row['price']
        
    