#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    q = "select name from sqlite_master where type='table'"
    cur.execute(q)
    
    rows = cur.fetchall()
    
    for row in rows:
        print row[0]
        