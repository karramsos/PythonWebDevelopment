#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import time

print "Unix time:", int(time.time())

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT strftime('%s', 'now')")
    
    r = cur.fetchone()[0]
    print "Unix time:", r
