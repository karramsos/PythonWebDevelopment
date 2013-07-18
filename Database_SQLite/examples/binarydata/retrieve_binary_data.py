#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()     
    
    cur.execute("SELECT Data FROM BinaryData WHERE Id=1")
    r = cur.fetchone()[0]
    
    print repr(str(r))
    print str(r).encode('hex')