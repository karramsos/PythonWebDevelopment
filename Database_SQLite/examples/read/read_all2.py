#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor()     
    cur.execute("SELECT Name, Price FROM Cars LIMIT 5")
    
    while True:
      
        row = cur.fetchone()
      
        if row == None:
          break
        
        print row[0], row[1]
     
    
          
