#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

eng = create_engine('sqlite:///allsortsDB.db')

Base = declarative_base()

class Car(Base):
    
    __tablename__ = "Cars"
    
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)
    
Session = sessionmaker(bind=eng)
ses = Session()

c1 = Car(Name='Oldsmobile', Price=23450)
ses.add(c1)
ses.commit()

res = ses.query(Car).all()

for car in res:
    print car.Name, car.Price

