#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
       
    cur.execute("PRAGMA foreign_keys=1")       
    cur.execute("DELETE FROM Authors WHERE AuthorId=2")    
    