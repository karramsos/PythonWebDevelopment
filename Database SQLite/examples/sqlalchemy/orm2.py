#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship


eng = create_engine('sqlite:///test.db')

Base = declarative_base()
 
class Author(Base):
    __tablename__ = "Authors"
 
    AuthorId = Column(Integer, primary_key=True)
    Name = Column(String)  
    Books = relationship("Book")


class Book(Base):
    __tablename__ = "Books"
 
    BookId = Column(Integer, primary_key=True)
    Title = Column(String)      
    AuthorId = Column(Integer, ForeignKey("Authors.AuthorId"))    
                           
    Author = relationship("Author")                           
         

Session = sessionmaker(bind=eng)
ses = Session()   

res = ses.query(Author).filter(Author.Name=="Leo Tolstoy").first()

for book in res.Books:
    print book.Title

res = ses.query(Book).filter(Book.Title=="Emma").first()    
print res.Author.Name  
  
 
