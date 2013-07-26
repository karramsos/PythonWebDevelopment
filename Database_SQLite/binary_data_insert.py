#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

bn = """\x812\xa3\xa5\xa9\x13(S\xae\x13a\x13\xd4\x90\x8c:}
Eq\xa2\xa1\xa7\xa7QA\xc7IYRT\xd8\x85\x0e0\x96=\x88\x98T\xa8
\x92\t\xa6\x0e """

con = lite.connect('allsortsDB.db')

with con:
    
    cur = con.cursor()
    
    sql = """
    create table if not exists BinaryData(Id integer primary key, Data blob)
    """
    
    cur.execute(sql)
    
    sql = "insert into BinaryData(Data) values (?)"
    cur.execute(sql, (buffer(bn), ))
