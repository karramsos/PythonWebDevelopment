#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    cur.execute('select name, price from cars limit 5')
    
    while True:
        
        row = cur.fetchone()
        
        if row == None:
            break
        
        print row[0], row[1]
