#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.executescript("""
        CREATE TABLE Words(Word TEXT);
        INSERT INTO Words VALUES('elite');
        INSERT INTO Words VALUES('frost');
        INSERT INTO Words VALUES('alpha');
        INSERT INTO Words VALUES('car');
        INSERT INTO Words VALUES('dolphin');
        INSERT INTO Words VALUES('bus');
        INSERT INTO Words VALUES('ghost');
    """) 
    
    sql = "SELECT Word FROM Words ORDER BY Word ASC"
    cur.execute(sql)
    
    for r in cur.fetchall():
        print r[0]