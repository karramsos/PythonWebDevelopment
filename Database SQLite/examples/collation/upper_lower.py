#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


def upper(a):
    return a.upper()
    
def lower(b):
    return b.lower()


con = lite.connect(':memory:')

con.create_function('UPPER', 1, upper)
con.create_function('LOWER', 1, lower)

with con:
             
    cur = con.cursor()    
    cur.execute("SELECT UPPER('ďateľ')")
    print cur.fetchone()[0]

    cur.execute("SELECT LOWER('ČUČORIEDKY')")
    print cur.fetchone()[0]    
    
    
        