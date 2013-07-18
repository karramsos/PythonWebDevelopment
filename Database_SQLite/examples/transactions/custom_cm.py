#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
   
        
class MyConn(lite.Connection):
    
    def __enter__(self):
        
        self.execute("BEGIN")
        return self
        
    def __exit__(self, exc_type, exc_info, traceback):

        if exc_type is None:
            self.execute("COMMIT")
        else:
            self.execute("ROLLBACK")


con = lite.connect('test.db', factory=MyConn)
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
    
for row in con.execute("SELECT * FROM Friends"):
    print row
  
