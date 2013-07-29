#!/usr/bin/env python
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

con = lite.connect('allsortsDB.db', factory=MyConn)
con.isolation_level = None

cur = con.cursor()

with con:
    cur.execute("drop table if exists Friends")
    cur.execute('''create table Friends(Id integer primary key, Name text)''')
    

try:
    cur.execute("insert into friends(name) values('Tom')")
    cur.execute("insert into Friends(name) values('Rebecca')")
    
    with con:
        
        cur.execute("insert into friends(name) values('Jim')")
        cur.execute("insert into friends(name) values('Rebecca')")
        raise Exception
    
except:
    print "There was an error"
    
for row in con.execute("select * from friends"):
    print row
