#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("select data from binarydata where id=1")
    r = cur.fetchone()[0]
    
    print repr(str(r))
    print str(r).encode('hex')