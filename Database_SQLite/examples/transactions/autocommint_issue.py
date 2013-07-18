#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
   
    
con = lite.connect('test.db')
con.isolation_level = None

cur = con.cursor()  
    
with con:  
    cur.execute("DROP TABLE IF EXISTS FRIENDS")
    cur.execute('''CREATE TABLE Friends(Id INTEGER PRIMARY KEY, 
        Name TEXT)''')
    
try:
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom')")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')")
    
    with con:
        
        cur.execute("INSERT INTO Friends(Name) VALUES ('Jim')")
        cur.execute("INSERT INTO Friends(Name) VALUES ('Robert')")
        raise Exception
  
except:
    
    print "There was an error"
      
for row in cur.execute("SELECT * FROM Friends"):
    print row
  

