#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import random

con = lite.connect('test.db')    


def rand_gen(n):
    
    for i in range(n):
        r = random.randint(0, 1000)
        yield (r, )       


with con:
          
    cur = con.cursor() 
    cur.executescript("""
        DROP TABLE IF EXISTS Random;
        CREATE TABLE Random(Val INT);
        """)
        
    rg = rand_gen(6)
    cur.executemany("INSERT INTO Random VALUES(?)", rg)
