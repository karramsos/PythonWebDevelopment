#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("select date()")
    print cur.fetchone()[0]
    
    cur.execute("select strftime('%d.%m.%Y')")
    print cur.fetchone()[0]
    
    cur.execute("select strftime('%Y-%m-%d %H:%M:%S')")
    print cur.fetchone()[0]
    
    sql = """select 'Days toXMas: ' || (strftime('%j', '2013-12-24') - strftime('%j', 'now'))"""
    cur.execute(sql)
    print cur.fetchone()[0]