#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:')

with con:
    
    cur = con.cursor()
    cur.execute("create table Friends(Id int primary key, \
                Name text)")
    cur.execute("insert into friends(name) values('Tom')")
    cur.execute("insert into friends(name) values('Beca')")
    cur.execute("insert into friends(name) values('Jim')")
    cur.execute("insert into friends(name) values('Robert')")
    
    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid
    