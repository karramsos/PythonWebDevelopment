#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def readImage():
    
    fin = open('beckov.jpg', 'rb')
    
    with fin:
        
        img = fin.read()
        return img

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    data = readImage()
    binary = lite.Binary(data)
    cur.execute("insert into images(Data) values (?)", (binary,))
    
