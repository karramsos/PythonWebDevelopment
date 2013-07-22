#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

a = "'Audi'; drop table cars;"

with con:
    
    cur = con.cursor()
    sql = "select * from cars where Name=%s" % a
    cur.executescript(sql)
    
    data = cur.fetchone()
    
    print data
    