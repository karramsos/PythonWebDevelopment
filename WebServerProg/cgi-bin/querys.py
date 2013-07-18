#!/usr/bin/env python
# If using Linux remember to chmod a+x querys.py

import cgi, os, sys

sys.stdout.write("Content-type: text.html\r\n\r\n")
sys.stdout.write("")
sys.stdout.write("<html><body>")
sys.stdout.write("<h2>Query String</h2>")

form = cgi.FieldStorage()
for field in form.keys():
	sys.stdout.write("%s -> %s<br />" % (field, form[field].value))
sys.stdout.write("</body></html>")