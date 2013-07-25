#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect(':memory:', detect_types = lite.PARSE_COLNAMES)

with con:
    
    cur = con.cursor()
    
    cur.executescript("""
                      create table Stamps2(Stamp timestamp);
                      insert into stamps2 values('2013-02-05 23:23:00');
                      insert into stamps2 values('2012-10-13 12:33:12');
                      insert into stamps2 values('2012-05-11T23:20:40');
                      insert into stamps2 values('2010-11-12 18:18:00');
                      """)
    
    sql = """select min(Stamp) as "Stamp [TIMESTAMP]" from stamps2"""
    cur.execute(sql)
    
    e = cur.fetchone()[0]
    print e, type(e)