#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import random

con = lite.connect('allsortsDB.db')

def rand_gen(n):
    
    for i in range(n):
        r = random.randint(0, 1000)
        yield (r, )
        
        
with con:
    
    cur = con.cursor()
    cur.executescript("""
                    drop table if exists Random;
                    create table Random(Val int);
                      """)
    
    rg = rand_gen(6)
    cur.executemany("insert into Random values(?)", rg)
    
        
    