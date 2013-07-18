#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

eng = create_engine('sqlite:///:memory:')

con = eng.connect()
con.execute('CREATE TABLE Cars(Id INTEGER PRIMARY KEY, \
Name TEXT, Price INTEGER)')

con.execute('INSERT INTO Cars(Name, Price) VALUES(?, ?)', 
           ('Audi',52642), ('Mercedes',57127), 
           ('Skoda',9000), ('Volvo',29000), 
           ('Bentley',350000), ('Citroen',21000), 
           ('Hummer',41400), ('Volkswagen',21600), 
)

ids = (1, 2, 3, 4, 5, 6)
sql = "SELECT * FROM Cars WHERE Id IN (?, ?, ?, ?, ?, ?)"
res = con.execute(sql, ids)

for row in res:
    print row[0], row[1], row[2]
    
con.close()