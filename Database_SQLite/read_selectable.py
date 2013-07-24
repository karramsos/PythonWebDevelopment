#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute('select * from cars')
    
    while True:
        
        rows = cur.fetchmany(3)
        
        if not rows:
            break
        
        print '*****************'
        
        for cid, name, price in rows:
            print cid, name, price