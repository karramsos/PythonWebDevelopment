#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars LIMIT 3")
    
    dc = cur.description
    print dc[0][0], dc[1][0], dc[2][0]