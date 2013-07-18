#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.executescript("""
        CREATE TABLE Dates(mdate TEXT);
        INSERT INTO Dates VALUES ('2013-02-05');
        INSERT INTO Dates VALUES ('2012-10-13 12:33:12');
        INSERT INTO Dates VALUES ('2012-05-11T23:20:40');
        INSERT INTO Dates VALUES ('13:23:04');
        """)        
    
    sql = "SELECT datetime(mdate, '7 hours') FROM dates"
    cur.execute(sql)
    
    for r in cur.fetchall():
        print r[0]
        
        
#SELECT DATE(the_date, '+1 year') FROM dates ORDER BY the_date;        
        
    

