#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

class Median(object):
    
    def __init__(self): 
        
        self.d = []
    
    def step(self, value):
        
        self.d.append(value)
    
    def finalize(self):
        
        n = len(self.d)
        mid = n / 2
        self.d.sort()
        
        if (n % 2) == 0:
            return (self.d[mid-1] + self.d[mid]) / 2.0
        else:
            return self.d[mid]
    
con = lite.connect(':memory:')

with con:
    
    con.create_aggregate('Median', 1, Median)
    
    cur = con.cursor()
    
    sql = """
    create table Vals(Id int, Age int, Height int);
    insert into vals values(1, 44, 178);
    insert into vals values(2, 32, 163);
    insert into vals values(3, 65, 184);
    insert into vals values(4, 54, 190);
    insert into vals values(5, 32, 190);
    insert into vals values(6, 28, 166);
    insert into vals values(7, 38, 175);
    insert into vals values(8, 40, 187);
    insert into vals values(9, 61, 183);
    insert into vals values(10, 18, 177);
    insert into vals values(11, 23, 170);
    """
    
    cur.executescript(sql)
    
    cur.execute("select median(age) from vals")
    r = cur.fetchone()[0]
    print r
    
    cur.execute("select median(height) from vals")
    
    r = cur.fetchone()[0]
    print r
    
    cur.execute("select median(age) from vals where id < 11")
    r = cur.fetchone()[0]
    print r
    
    
