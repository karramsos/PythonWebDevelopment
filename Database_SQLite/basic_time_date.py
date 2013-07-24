#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("select time('now')")
    print cur.fetchone()[0]
    
    cur.execute("select date()")
    print cur.fetchone()[0]
    
    cur.execute("select datetime()")
    print cur.fetchone()[0]
    
    cur.execute("select date('now', '-22 days')")
    print cur.fetchone()[0]
    
    cur.execute("select time('now', '4 hours')")
    print cur.fetchone()[0]
    
    cur.execute("select date('now', 'start of year')")
    print cur.fetchone()[0]
    
    cur.execute("select date('now', 'weekday 6')")
    print cur.fetchone()[0]
    
    cur.execute("""select date('now', 'start of year', '8 months', 'weekday 4')""")
    print cur.fetchone()[0]
    
    
    