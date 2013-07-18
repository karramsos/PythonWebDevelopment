#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def writeImage(data):
    
    fout = open('beckov2.jpg','wb')
    
    with fout:
        
        fout.write(data)      
    

con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT Data FROM Images LIMIT 1")
    data = cur.fetchone()[0]
    
    writeImage(data)

    
   