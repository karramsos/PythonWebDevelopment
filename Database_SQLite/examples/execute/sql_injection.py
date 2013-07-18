#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


con = lite.connect('test.db')    

a = "'Audi';DROP TABLE Cars;"

with con:
          
    cur = con.cursor() 
    sql = "SELECT * FROM Cars WHERE Name=%s" % a
    cur.executescript(sql)

    data = cur.fetchone()

    print data