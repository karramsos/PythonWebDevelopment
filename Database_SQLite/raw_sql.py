#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine('sqlite:///allsortsDB.db')
con = eng.connect()

res = con.execute("select * from Cars limit 4")

for row in res:
    print row['Id'], row['Name'], row['Price']
    
con.close()