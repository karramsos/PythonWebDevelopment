#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import random

con = lite.connect('test.db')    

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
        DROP TABLE IF EXISTS Random;
        CREATE TABLE Random(Val INT);
        """)
    
    ri = RandIt(5)
    cur.executemany("INSERT INTO Random VALUES(?)", ri)
