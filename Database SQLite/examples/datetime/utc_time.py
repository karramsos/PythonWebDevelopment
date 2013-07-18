#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()    
    
    cur.execute("SELECT datetime()")
    utc_time = cur.fetchone()[0]

    print "Universal time:", utc_time
    
    sql = "SELECT datetime(current_timestamp, 'localtime')"
    cur.execute(sql)
    loc_time = cur.fetchone()[0]

    print "Local time:", loc_time    