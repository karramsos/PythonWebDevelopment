#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    
    cur.execute("SELECT Price FROM Cars WHERE Name='Volvo'")    
    r = cur.fetchone()[0]
    
    print "The price of Volvo:", r
