#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    sql = 'select * from cars'
    
    for cid, name, price in cur.execute(sql):
        print cid, name, price
    