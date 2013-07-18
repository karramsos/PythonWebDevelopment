#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("SELECT time('now')")
    print cur.fetchone()[0]
    
    cur.execute("SELECT date()")
    print cur.fetchone()[0]
    
    cur.execute("SELECT datetime()")
    print cur.fetchone()[0]    

    cur.execute("SELECT date('now', '-22 days')")
    print cur.fetchone()[0]       
    
    cur.execute("SELECT time('now', '4 hours')")
    print cur.fetchone()[0]   
    
    cur.execute("SELECT date('now', 'start of year')")
    print cur.fetchone()[0]    

    cur.execute("SELECT date('now', 'weekday 6')")
    print cur.fetchone()[0]       
    
    cur.execute("""SELECT date('now', 'start of year', 
        '8 months', 'weekday 4')""")
    print cur.fetchone()[0]       