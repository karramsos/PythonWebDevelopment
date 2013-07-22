#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.execute("select 55")
    val = cur.fetchone()[0]
    print val, type(val)
    
    cur.execute("select 125*12510*12510")
    val = cur.fetchone()[0]
    print val, type(val)
    
    cur.execute("select 12 + 3.4")
    val = cur.fetchone()[0]
    print val, type(val)