#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    
    cur.execute('pragma encoding')
    val = cur.fetchone()[0]
    print val
    
    cur.execute("pragma foreign_keys")
    val = cur.fetchone()[0]
    print val