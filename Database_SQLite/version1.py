#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect(':memory:')
    
    cur = con.cursor()
    cur.execute('SELECT sqlite_version()')
    
    data = cur.fetchone()
    
    print "SQLite version:", data[0]
    
except lite.Error, e:
    
    print "Error %s" % e.args[0]
    sys.exit(1)

finally:
    
    if con:
        con.close()