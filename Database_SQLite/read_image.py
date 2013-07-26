#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def writeImage(data):
    
    fout = open('beckov.jpg', 'wb')
    
    with fout:
        
        fout.write(data)

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    cur.execute("select data from images limit 1")
    data = cur.fetchone()[0]
    
    writeImage(data)
    
