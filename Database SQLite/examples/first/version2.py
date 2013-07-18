#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.execute('SELECT sqlite_version()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data 