import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into films values("Annie Hall", "1977", "Woody Allen")')
cursor.execute('insert into films values("The Godfather", "1972" ,"Francis Ford Coppola")')
