#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute('select * from cars')
    rows = cur.fetchall()
    
    for row in rows:
        print row[0], " - ", row[1], " - ", row[2]
