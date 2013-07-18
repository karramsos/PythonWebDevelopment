import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("drop table if exists temps")
cursor.execute("create table temps(date text, temp int)")
cursor.execute('insert into temps values("12/1/2011", 35)')
cursor.execute('insert into temps values("12/2/2011", 42)')
cursor.execute('insert into temps values("12/3/2011", 38)')
cursor.execute('insert into temps values("12/4/2011", 41)')
cursor.execute('insert into temps values("12/5/2011", 40)')
cursor.execute('insert into temps values("12/6/2011", 28)')
cursor.execute('insert into temps values("12/7/2011", 45)')
conn.row_factory = db.Row
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
	print("%s %s" % (row[0], row[1]))
cursor.execute("select avg(temp) from temps")
row = cursor.fetchone()
print("The average temprature for the week was %s" % row[0])
cursor.execute("delete from temps where temp = 40")
cursor.execute("select * from temps")
rows = cursor.fetchall()
for row in rows:
	print("%s %s" % (row[0], row[1]))