#!/usr/bin/python
# -*- coding: utf -8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

eng = create_engine('sqlite:///allsortsDB.db')
Base = declarative_base(eng)

class Author(Base):
    
    __tablename__ = 'Authors'
    __table_args__ = {'autoload': True}
    
class Book(Base):
    
    __tablename__ = 'Books'
    __table_args__ = {'autoload': True}

metadata = Base.metadata

for table in metadata.sorted_tables:
    
    for col in table.columns.keys():
        print col
    
