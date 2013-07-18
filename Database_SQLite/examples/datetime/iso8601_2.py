#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.executescript("""
        CREATE TABLE Dates(mdate TEXT);
        INSERT INTO Dates VALUES ('2013-02-05');
        INSERT INTO Dates VALUES ('2012-10-13');
        INSERT INTO Dates VALUES ('2012-05-11');
        INSERT INTO Dates VALUES ('2012-11-01');
        INSERT INTO Dates VALUES ('2013-01-26');
        """)
        
    cur.execute("SELECT MIN(mdate) FROM Dates")
    r = cur.fetchone()[0]
    print r
    
    print "**********************"
    
    cur.execute("SELECT MAX(mdate) FROM Dates")
    r = cur.fetchone()[0]
    print r
    
    print "**********************"
    
    cur.execute("SELECT mdate FROM dates ORDER BY mdate")
    
    for r in cur.fetchall():
        print r[0]
        
        
#SELECT DATE(the_date, '+1 year') FROM dates ORDER BY the_date;        
        
    

