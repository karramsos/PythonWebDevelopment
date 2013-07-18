#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
 
con = lite.connect('allsortsDB.db')

with con :
    
    cur = con.cursor()
    cur.execute("drop table if exists Cars")
    cur.execute("create table Cars(Id int, Name Text, Price int)")
    cur.execute("insert into Cars values(1, 'Audi', 52642)")
    cur.execute("insert into Cars values(2, 'Mercedes', 57127)")
    cur.execute("insert into Cars values(3, 'Skoda', 9000)")
    cur.execute("insert into Cars values(4, 'Volvo', 29000)")
    cur.execute("insert into Cars values(5, 'Bentley', 350000)")
    cur.execute("insert into Cars values(6, 'Citroen', 21000)")
    cur.execute("insert into Cars values(7, 'Hummer', 41400)")
    cur.execute("insert into Cars values(8, 'Volkswagen', 21600)")
    
 
