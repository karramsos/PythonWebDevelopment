#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine('sqlite:///allsortsDB.db')

con = eng.connect()
con.execute('drop table if exists Cars')
con.execute('create table Cars(Id integer primary key, \
            Name text, Price integer)')

con.execute('insert into Cars(Name, Price) values(?, ?)',
            ('Audi', 52642), ('Mercedes', 57127),
            ('Skoda', 9000), ('Volvo', 29000),
            ('Bentley', 350000), ('Citroen', 21000),
            ('Hummer', 41400), ('Volkswagen', 21600),
           )

ids = (1,2,3,4,5,6)
sql = "select * from Cars where Id in (?,?,?,?,?,?)"
res = con.execute(sql, ids)

for row in res:
    print row[0], row[1], row[2]

con.close()