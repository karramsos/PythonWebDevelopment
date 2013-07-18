#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    
    cur.execute("SELECT count(Id) FROM Cars")

    r = cur.fetchone()
    print r, type(r)    
