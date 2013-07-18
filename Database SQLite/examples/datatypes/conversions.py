#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()        

    cur.execute("SELECT 55")
    val = cur.fetchone()[0]
    print val, type(val)

    cur.execute("SELECT 125*12510*12510")
    val = cur.fetchone()[0]
    print val, type(val)    
    
    cur.execute("SELECT 12 + 3.4")
    val = cur.fetchone()[0]
    print val, type(val)    
    
    