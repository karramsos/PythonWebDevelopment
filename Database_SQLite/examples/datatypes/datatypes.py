#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

a = 12
b = 3.434
c = "ZetCode"
d = buffer(c)

with con:
        
    cur = con.cursor()        
    cur.execute("INSERT INTO DataTypes VALUES(?, ?, ?, ?)", 
        (a, b, c, d))
    cur.execute("INSERT INTO DataTypes VALUES(?, ?, ?, ?)", 
        (None, None, None, None))
