#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    
    sql = "SELECT * FROM Cars"    
    
    for cid, name, price in cur.execute(sql):
        print cid, name, price