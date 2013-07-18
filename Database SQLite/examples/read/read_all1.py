#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    
    cur.execute("SELECT * FROM Cars")
    rows = cur.fetchall()
      
    #print rows, type(rows)  
    
    for row in rows:
        print row[0], row[1], row[2]
          
