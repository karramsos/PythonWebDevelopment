#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:', detect_types = lite.PARSE_DECLTYPES)

with con:
    
    cur = con.cursor()
    
    cur.execute("create table Stamps(Stamp Timestamp)")
    sql = "insert into stamps values('2012-11-10 23:12:08')"
    cur.execute(sql)
    
    cur.execute("select stamp from stamps")
    
    e = cur.fetchone()[0]
    print e, type(e)