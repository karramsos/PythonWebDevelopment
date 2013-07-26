#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

svk = [u'a', u'?', u'?', u'b', u'c', u'?', u'd', u'?',
u'dz', u'd?', u'e', u'?', u'f', u'g', u'h', u'ch', u'i',
u'?', u'j', u'k', u'l', u'?', u'?', u'm', u'n', u'?',
u'o', u'?', u'?', u'p', u'q', u'r', u'?', u's', u'?',
u't', u'?', u'u', u'?', u'v', u'w', u'x', u'y', u'?',
u'z', u'?']

def svk_col(a, b):
    
    a = a.decode('utf-8')
    b = b.decode('utf-8')
    
    l1, l2 = len(a), len(b)
    
    l = min(l1, l2)
    
    for i in range(l):
        
        x = svk.index(a[i])
        y = svk.index(b[i])
        z = cmp(x, y)
        
        if z == 0:
            continue
        else:
            return z
    
    if l1 > l2:
        return 1
    else:
        return -1

con = lite.connect(':memory:')
con.create_collation('SLOVAK', svk_col)

with con:
    
    cur = con.cursor()
    
    words = ((u'?ava', ), (u'sneh', ), (u'cena ', ),
    (u'zem', ), (u'?repy', ), (u'?ula', ), (u'auto ', ),
    (u'automobil ', ), (u'ban?n', ), (u'tovar ' ,), (u'?um', ),
    (u'?rep', ))
    
    sql = "create table Words4(Word text collate slovak)"
    cur.execute(sql)
    
    cur.executemany("insert into words4 values (?)", words)
    cur.execute("select word from words4 order by word")
    
    for r in cur.fetchall():
        print r[0]
    
