#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def authorizer(sqltype, arg1, arg2, dbname, source):
    
    if sqltype == lite.SQLITE_SELECT:
        
        return lite.SQLITE_OK
        
    elif sqltype == lite.SQLITE_READ:
        
        if arg2 == 'Id':
            return lite.SQLITE_OK
        elif arg2 == 'Name':
            return lite.SQLITE_OK
        elif arg2 == 'Salary':
            return lite.SQLITE_IGNORE
    
con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    con.set_authorizer(authorizer)
    
    cur.execute("select * from Salaries")
    
    for row in cur.fetchall():
        
        print row[0], row[1], row[2]
    
