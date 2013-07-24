#!/usr/bin/env python
# If using Linux remember to chmod a+x updatefilms.py

import cgi, sys, os
import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
filmdata = cgi.FieldStorage()
title = filmdata["title"].value
year = filmdata["year"].value
director = filmdata["director"].value
cursor.execute('update films set year = ? where title = ?', (year, title))
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()

sys.stdout.write("Content-type: text/html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body><h1>Films</h1><p>")
for row in rows:
	sys.stdout.write("%s %s %s" % (row[0], row[1], row[2]))
	sys.stdout.write("<br />")
sys.stdout.write("</p></body></html>")