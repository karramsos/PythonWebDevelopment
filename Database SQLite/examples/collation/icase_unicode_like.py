#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

    
def like(a, b):
       
    x = a.lower()
    y = b.lower()        
        
    z = cmp(x, y)
    
    if z == 0:
        return True
    else:
        return False
        

con = lite.connect(':memory:')


with con:
             
    cur = con.cursor()    
    
    con.create_function('LIKE', 2, like)
   
    cur.executescript("""
        CREATE TABLE Words(Word TEXT);
        INSERT INTO Words VALUES ('ťava'); 
        INSERT INTO Words VALUES ('ťažký');
        INSERT INTO Words VALUES ('Ťažký'); 
        INSERT INTO Words VALUES ('turbína');
        INSERT INTO Words VALUES ('trieska'); 
        INSERT INTO Words VALUES ('cement');
        INSERT INTO Words VALUES ('cvikla');
        INSERT INTO Words VALUES ('armáda');
        """)

    cur.execute("SELECT Word FROM Words WHERE Word LIKE 'ťažký'")
    
    for r in cur.fetchall():
        print r[0]
    
    
    