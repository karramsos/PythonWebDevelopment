#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

new_car = ('BMW', '33400')

with con:
    
    cur = con.cursor()
    
    sql = "insert into cars(Name, Price) values(?, ?)"
    
    cur.execute(sql, new_car)
    