#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite


class Car(object):
    
    def __init__(self, cid, name, price):
        
        self.cid = cid
        self.name = name
        self.price = price


def adapt_car(car):
    
    return "%d;%s;%d" % (car.cid, car.name, car.price)


lite.register_adapter(Car, adapt_car)        
        
con = lite.connect(':memory:')

c1 = Car(1, 'Audi', 52642)
c2 = Car(2, 'Mercedes', 57127)
c3 = Car(3, 'Skoda', 9000)

with con:   
    
    cur = con.cursor()
    cur.execute("CREATE TABLE Cars(c Car)")  
    cur.execute("INSERT INTO Cars VALUES(?)", (c1,))
    cur.execute("INSERT INTO Cars VALUES(?)", (c2,))
    cur.execute("INSERT INTO Cars VALUES(?)", (c3,))
    
    cur.execute("SELECT * FROM Cars")  

    for row in cur.fetchall():
        print row[0]
