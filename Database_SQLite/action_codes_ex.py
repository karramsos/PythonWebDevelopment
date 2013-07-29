#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def authorizer(sqltype, arg1, arg2, dbname, source):
    
    if sqltype == lite.SQLITE_CREATE_TABLE:
        print 'Crating table', arg1
        return lite.SQLITE_OK
    
    elif sqltype == lite.SQLITE_READ:
        print 'Accessing column %s.%s from %s' % \
        (arg1, arg2, dbname)
        return lite.SQLITE_OK
    
    elif sqltype == lite.SQLITE_INSERT:
        print 'Inserting into', arg1
        return lite.SQLITE_OK
        
    elif sqltype == lite.SQLITE_UPDATE:
        print 'Updating %s.%s' % (arg1, arg2)
        return lite.SQLITE_OK
    
    elif sqltype == lite.SQLITE_DELETE:
        print 'Dropping table', arg1
        return lite.SQLITE_OK
    
    elif sqltype == lite.SQLITE_DROP_TABLE:
        print 'Dropping table', arg1
        return lite.SQLITE_OK
    
lite.enable_callback_tracebacks(True)
con = lite.connect('allsortsDB.db')

with con:
        
    cur = con.cursor()
    
    con.set_authorizer(authorizer)
    
    sql = """
    drop table if exists Salaries;
    create table Salaries(Id int, Name text, Salary int);
    insert into salaries values(1, 'Tom', 5400);
    insert into salaries values(2, 'Frank', 4230);
    insert into salaries values(3, 'Jane', 3230);
    insert into salaries values(4, 'Samuel', 3800);
    """
    
    cur.executescript(sql)
        
        
