#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')   

with con:
    
    cur = con.cursor()
    
    cur.execute("SELECT Name FROM Cars WHERE Id=?", (1, ))
    val = cur.fetchone()
    
    print val[0]