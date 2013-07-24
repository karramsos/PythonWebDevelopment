#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("pragma foreign_keys")
    cs = cur.fetchone()
    
    print "Foreign keys: %d" % cs
    
    cur.execute("pragma foreign_keys = 1")
    cur.execute("pragma foreign_keys")
    cs = cur.fetchone()
    
    print "Foreign keys: %d" % cs