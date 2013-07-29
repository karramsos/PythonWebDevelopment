#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = lite.connect('allsortsDB.db')
con.isolation_level = None

try:
    
    con.execute("begin transaction")
    con.execute("drop table if exists Ints")
    con.execute("create table Ints(i int)")
    con.execute("insert into Ints values(1)")
    con.execute("savepoint sp1")
    con.execute("insert into ints values(2)")
    con.execute("savepoint sp2")
    con.execute("insert into Ints values(5)")
    con.execute("rollback transaction to sp2")
    con.execute("release sp1")
    #con.execute("realese sp2")
    con.execute("commit")
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:
    
    if con:
        con.close()