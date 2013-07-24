#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute("pragma foreign_keys = 1")
    #cur.execute("delete from books where bookid in (2,6)")
    cur.execute("delete from authors where authorid = 2 ")
    