#!/usr/bin/env python
# If using Linux remember to chmod a+x hellocgi.py

import cgi, os, sys
sys.stdout.write("Content-type: text.html \r\n\r\n")
sys.stdout.write("<!doctype html><html><head><title>Hello CGI</title></head>")
sys.stdout.write("<body><h2>Hello CGI</h2></body></html>")