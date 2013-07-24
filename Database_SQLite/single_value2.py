#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("select price from cars where name='Volvo'")
    r = cur.fetchone()[0]
    
    print "The price of Volvo:", r