#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

        
class Median(object):
    
    def __init__(self):
        
        self.d = []

    def step(self, value):
        
        self.d.append(value)

    def finalize(self):
        
        n = len(self.d)
        mid = n / 2
        self.d.sort()
        
        if (n % 2) == 0:
            return (self.d[mid-1] + self.d[mid]) / 2.0
        else:
            return self.d[mid]        
    
con = lite.connect(':memory:')    
    
with con:
    
    con.create_aggregate('Median', 1, Median)
        
    cur = con.cursor()    
    
    sql = """
    CREATE TABLE Vals(Id INT, Age INT, Height INT);
    INSERT INTO Vals VALUES(1, 44, 178);
    INSERT INTO Vals VALUES(2, 32, 163);
    INSERT INTO Vals VALUES(3, 65, 184);
    INSERT INTO Vals VALUES(4, 54, 190);
    INSERT INTO Vals VALUES(5, 32, 157);
    INSERT INTO Vals VALUES(6, 28, 166);
    INSERT INTO Vals VALUES(7, 38, 175);
    INSERT INTO Vals VALUES(8, 40, 187);
    INSERT INTO Vals VALUES(9, 61, 183);
    INSERT INTO Vals VALUES(10, 18, 177);
    INSERT INTO Vals VALUES(11, 23, 170);
    """    
    
    cur.executescript(sql) 
       
    cur.execute("SELECT Median(Age) FROM Vals")
    r = cur.fetchone()[0]
    print r
    
    cur.execute("SELECT Median(Height) FROM Vals")
    r = cur.fetchone()[0]
    print r    

    cur.execute("SELECT Median(Age) FROM Vals WHERE Id < 11")
    r = cur.fetchone()[0]
    print r
            
                 