#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Citroen', 21000),
    (7, 'Hummer', 41499),
    (8, 'Volkswagen', 21600)
    
)

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    cur.execute('drop table if exists cars')
    cur.execute('create table Cars(Id integer primary key, \
                Name text, Price int)')
    cur.executemany('insert into cars values(?, ?, ?)', cars)