#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("SELECT date()")
    print cur.fetchone()[0]
    
    cur.execute("SELECT strftime('%d.%m.%Y')")
    print cur.fetchone()[0]
    
    cur.execute("SELECT strftime('%Y-%m-%d %H:%M:%S')")
    print cur.fetchone()[0]    
    
    sql = """SELECT 'Days to XMas: ' || 
    (strftime('%j', '2013-12-24') - strftime('%j', 'now'))"""           
    cur.execute(sql)
    print cur.fetchone()[0]         