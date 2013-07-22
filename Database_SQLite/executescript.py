#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

con = lite.connect('allsortsDB.db')

with con:
    cur = con.cursor()
    
    cur.executescript("""
                    drop table if exists cars;
                    create table Cars(Id integer primary key,
                        Name text, Price int);
                    insert into cars values(1, 'Audi' ,52642);
                    insert into cars values(2, 'Mercedes', 57127);
                    insert into cars values(3, 'Skoda', 9000);
                    insert into cars values(4, 'Volvo', 29000);
                    insert into cars values(5, 'Bentley', 3500000);
                    insert into cars values(6, 'Citroen', 21000);
                    insert into cars values(7, 'Hummer', 41400);
                    insert into cars values(8, 'Volkswagen', 21600)
                      """)
 