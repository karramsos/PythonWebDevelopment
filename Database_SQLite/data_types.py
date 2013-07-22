#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

a = 12
b = 3.434
c = "ZetCode"
d = buffer(c)

with con:
    
    cur = con.cursor()
    cur.execute("insert into DataTypes values(?, ?, ?, ?)",
                (a,b,c,d))
    cur.execute("insert into DataTypes values(?, ?, ?, ?)",
                (None, None, None, None))