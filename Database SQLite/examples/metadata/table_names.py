#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    q = "SELECT name FROM sqlite_master WHERE type='table'"
    cur.execute(q)

    rows = cur.fetchall()

    for row in rows:
        print row[0]