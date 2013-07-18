#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


eng = create_engine('sqlite:///test.db')

Base = declarative_base(eng)
 
class Car(Base):
    
    __tablename__ = "Cars"
    __table_args__ = {'autoload':True}
    
car = Car()
s = car.__table__.select().where(car.__table__.c['Id']==3)

con = eng.connect()

res = con.execute(s)

for row in res:
    print row[0], row[1], row[2]
    
