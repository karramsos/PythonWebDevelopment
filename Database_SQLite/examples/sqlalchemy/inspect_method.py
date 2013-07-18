#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import inspect
from sqlalchemy import create_engine

eng = create_engine('sqlite:///test.db')
insp = inspect(eng)

for table in insp.get_table_names():
    print table
    
print insp.get_primary_keys("Cars")[0]
print insp.get_primary_keys("Authors")[0]

print insp.engine
print insp.dialect.name
print insp.dialect.dbapi.version

