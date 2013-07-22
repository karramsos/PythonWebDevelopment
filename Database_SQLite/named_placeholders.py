#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

uId = 6

with con:
    
    cur = con.cursor()
    
    sql = "select * from cars where Id=:Id"
    cur.execute(sql, {"Id": uId})
    
    data = cur.fetchone()
    print data