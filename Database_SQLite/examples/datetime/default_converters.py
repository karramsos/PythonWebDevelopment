#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:', 
    detect_types=lite.PARSE_DECLTYPES)

with con:
    
    cur = con.cursor()    
    
    cur.execute("CREATE TABLE Stamps(Stamp TIMESTAMP)")
    sql = "INSERT INTO Stamps VALUES('2012-11-10 23:12:08')"
    cur.execute(sql)

    cur.execute("SELECT Stamp FROM Stamps")
    
    e = cur.fetchone()[0]
    print e, type(e)
     
    

