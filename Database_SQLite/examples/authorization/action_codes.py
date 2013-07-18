#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


def authorizer(sqltype, arg1, arg2, dbname, source):
        
    #print sqltype
    
    if sqltype == lite.SQLITE_CREATE_TABLE:
        print 'Creating table', arg1
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
        print 'Deleting from', arg1
        return lite.SQLITE_OK   
        
    elif sqltype == lite.SQLITE_DROP_TABLE:
        print 'Dropping table', arg1
        return lite.SQLITE_OK      
        
    #elif sqltype == lite.SQLITE_TRANSACTION :
        #print 'Transaction', arg1
        #return lite.SQLITE_OK           


lite.enable_callback_tracebacks(True)
con = lite.connect('test.db')    

with con:
          
    cur = con.cursor() 
    
    con.set_authorizer(authorizer)
    
    sql = """
        DROP TABLE IF EXISTS Salaries;
        CREATE TABLE Salaries(Id INT, Name TEXT, Salary INT);
        INSERT INTO Salaries VALUES(1, 'Tom', 5400);
        INSERT INTO Salaries VALUES(2, 'Frank', 4230);
        INSERT INTO Salaries VALUES(3, 'Jane', 3230);
        INSERT INTO Salaries VALUES(4, 'Samuel', 3800);
    """    
    
    cur.executescript(sql)     


    