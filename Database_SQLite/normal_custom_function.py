#!/usr/bin/env python
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
    create table Messages(Id integer primary key, Message text)
    """
    
    cur.execute(sql)
    
    cur.executescript("""
                      insert into messages values(1, encrypt('Operation failed'));
                      insert into messages values(2, encrypt('Enemy spotted'));
                      insert into messages values(3, encrypt('Target hit'));
                      """)
    
    cur.execute("select message from messages where id=1")
    r = cur.fetchone()[0]
    print "Encrypted message Id-1: " + r
    cur.execute("select message from messages where id=2")
    r = cur.fetchone()[0]
    print "Encrypted message Id-2: " + r
    cur.execute("select message from messages where id=3")
    r = cur.fetchone()[0]
    print "Encrypted message Id-3: " + r
    
    sql = "select decrypt(message) from messages where Id=1"
    cur.execute(sql)
    r = cur.fetchone()[0]
    print "Decrypted message Id-1: " + r 
    sql = "select decrypt(message) from messages where Id=2"
    cur.execute(sql)
    r = cur.fetchone()[0]
    print "Decrypted message Id-2: " + r
    sql = "select decrypt(message) from messages where Id=3"
    cur.execute(sql)
    r = cur.fetchone()[0]
    print "Decrypted message Id-3: " + r
    
