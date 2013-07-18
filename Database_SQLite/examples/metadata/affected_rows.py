#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("DELETE FROM Cars")   

    print "There have been %d changes" % con.total_changes