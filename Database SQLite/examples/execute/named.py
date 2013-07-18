#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

uId = 6

with con:
          
    cur = con.cursor() 
    
    sql = "SELECT * FROM Cars WHERE Id=:Id"
    cur.execute(sql, {"Id": uId})
    
    data = cur.fetchone()
    print data

    