#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute('select name from cars where id=?', (1, ))
    val = cur.fetchone()
    
    print val[0]