#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import random

con = lite.connect('allsortsDB.db')

class RandIt:
    
    def __init__(self, n):
        self.count = 0
        self.n = n
        
    def __iter__(self):
        return self
    
    def next(self):
        
        self.count += 1
        
        if self.count > self.n:
            raise StopIteration
        
        return (random.randint(0, 1000), )
    
with con:
    
    cur = con.cursor()
    cur.executescript("""
                    drop table if exists Random;
                    create table Random(Val int);
                      """)
    
    ri = RandIt(5)
    cur.executemany("insert into Random values(?)", ri)
    
    