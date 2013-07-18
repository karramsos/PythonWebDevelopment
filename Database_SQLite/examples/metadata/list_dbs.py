#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    cur.execute("ATTACH DATABASE 'movies.db' AS movies")
    
    cur.execute("PRAGMA database_list")
    rows = cur.fetchall()

    for row in rows:
        print row[0], row[1], row[2]