#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('test.db')    

new_car = ('BMW', '33400')

with con:
          
    cur = con.cursor() 
    
    sql = "INSERT INTO Cars(Name, Price) VALUES(?, ?)"
    cur.execute(sql, new_car)

    