#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import datetime

con = lite.connect(':memory:')

d1 = datetime.datetime(2013, 1, 1, 15, 12, 0).isoformat() 
d2 = datetime.datetime.fromtimestamp(1360350273).isoformat()
d3 = datetime.datetime.now().isoformat()
d4 = datetime.datetime.utcnow().isoformat()

with con:
    
    cur = con.cursor()    
    
    cur.execute("CREATE TABLE Dates(mdate TEXT)") 
    cur.execute("INSERT INTO Dates VALUES(?)", (d1, ))
    cur.execute("INSERT INTO Dates VALUES(?)", (d2, ))
    cur.execute("INSERT INTO Dates VALUES(?)", (d3, ))
    cur.execute("INSERT INTO Dates VALUES(?)", (d4, ))
    
    cur.execute("SELECT mdate FROM dates")
    
    for r in cur.fetchall():
        print r[0]
        
        
    
        
    

