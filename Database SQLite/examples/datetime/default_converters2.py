#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:', 
    detect_types=lite.PARSE_COLNAMES)

with con:
    
    cur = con.cursor()    
    
    cur.executescript("""
        CREATE TABLE Stamps(Stamp TIMESTAMP);
        INSERT INTO Stamps VALUES ('2013-02-05 23:23:00');
        INSERT INTO Stamps VALUES ('2012-10-13 12:33:12');
        INSERT INTO Stamps VALUES ('2012-05-11T23:20:40');
        INSERT INTO Stamps VALUES ('2010-11-12 18:18:00');
        """)        

    sql = """SELECT MIN(Stamp) AS "Stamp [TIMESTAMP]" 
             FROM Stamps"""
    cur.execute(sql)
    
    e = cur.fetchone()[0]
    print e, type(e)
     
    

