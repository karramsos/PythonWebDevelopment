#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

eng = create_engine('sqlite:///allsortsDB.db')

Base = declarative_base(eng)

class Car(Base):
    
    __tablename__ = "Cars"
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)
    
con = eng.connect()

ins_car = Car.__table__.insert(
    values=dict(Name='Renault' , Price=18800)
)

con.execute(ins_car)

con.close()