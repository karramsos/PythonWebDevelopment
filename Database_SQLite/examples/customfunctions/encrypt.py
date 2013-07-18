#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

def encrypt(v):
    
    return v.encode('rot13')

def decrypt(v):
        
    return v.decode('rot13')


con = lite.connect(':memory:')    
    
with con:
    
    con.create_function('encrypt', 1, encrypt)
    con.create_function('decrypt', 1, decrypt)    
    
    cur = con.cursor()    
    
    sql = """
    CREATE TABLE Messages(Id INTEGER PRIMARY KEY, 
        Message TEXT)
    """    
    
    cur.execute(sql)    
    
    cur.executescript("""
    INSERT INTO Messages VALUES(1, encrypt('Operation failed'));
    INSERT INTO Messages VALUES(2, encrypt('Enemy spotted'));
    INSERT INTO Messages VALUES(3, encrypt('Target hit'));
    """)
    
    cur.execute("SELECT Message FROM Messages WHERE Id=3")
    r = cur.fetchone()[0]    
    print r
    
    sql = "SELECT decrypt(Message) FROM Messages WHERE Id=3"
    cur.execute(sql)
    r = cur.fetchone()[0]    
    print r
      