#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine('sqlite:///test.db')

con = eng.connect()

res = con.execute("SELECT * FROM Cars LIMIT 4")

for row in res:
    print row['Id'], row['Name'], row['Price']
    
con.close()