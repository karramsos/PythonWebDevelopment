#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
   con = lite.connect('allsortDB.db')
   cur = con.cursor()
   cur.execute("drop table if exists Friends")
   cur.execute('''create table Friends(Id integer primary key, Name text)''')
   cur.execute("insert into Friends(Name) values('Tom')")
   cur.execute("insert into friends(name) values('Rebecca')")
   cur.execute("insert into friends(name) values('Jim')")
   cur.execute("insert into friends(name) values('Robert')")
   
   cur.execute("create table if not exists Temporary(Id int)")
   
   
   
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
   
   