#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

svk = [u'a', u'á', u'ä', u'b', u'c', u'č', u'd', u'ď', 
u'dz', u'dž', u'e', u'é', u'f', u'g', u'h', u'ch', u'i', 
u'í', u'j', u'k', u'l', u'ľ', u'ĺ', u'm', u'n', u'ň', 
u'o', u'ó', u'ô', u'p', u'q', u'r', u'ŕ', u's', u'š', 
u't', u'ť', u'u', u'ú', u'v', u'w', u'x', u'y', u'ý', 
u'z', u'ž']

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
    
    words = ((u'ťava', ), (u'sneh', ), (u'cena', ), 
(u'zem', ), (u'črepy', ), (u'žula', ), (u'auto', ), 
(u'automobil', ), (u'banán', ), (u'tovar' ,), (u'šum', ), 
(u'črep', ))
    
    sql = "CREATE TABLE Words(Word TEXT COLLATE SLOVAK)"
    cur.execute(sql)
    
    cur.executemany("INSERT INTO Words VALUES(?)", words)    

    cur.execute("SELECT Word FROM Words ORDER BY Word")
    
    for r in cur.fetchall():
        print r[0]
    
    
    