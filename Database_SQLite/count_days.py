#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

borodino_battle = '1812-09-07'
slavkov_battle = '1805-12-02'

with con:
    
    cur = con.cursor()
    
    cur.execute("select julianday()")
    tdays = cur.fetchone()[0]
    
    cur.execute("select julianday(?)", (slavkov_battle,))
    sdays = cur.fetchone()[0]
    print "Days since Slavkov battle:", int(tdays - sdays)
    
    cur.execute("select julianday(?)", (borodino_battle,))
    bdays = cur.fetchone()[0]
    print "Days since Borodino battle:", int(tdays - bdays)