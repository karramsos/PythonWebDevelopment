import sqlite3 as db

conn = db.connect('test.db')
conn.row_factory = db.Row
cursor = conn.cursor()

cursor.execute("select * from films")
rows = cursor.fetchall()
for row in rows:
	print("%s %s %s" % (row["title"], row["year"], row["director"]))
conn.close()