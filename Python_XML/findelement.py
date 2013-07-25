#!/usr/bin/env python
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import string, sys

def trim(text):
	return ' '.join(text.split())

class FindContent(ContentHandler):

	def __init__(self, name):
		self.toFind = name
		self.inElement = 0
		self.found = ""

	def startElement(self, name, attrs):
		self.found = ""
		if name == self.toFind:
			self.inElement = 1
		else:
			self.inElement = 0

	def characters(self, ch):
		if self.inElement:
			self.found = self.found + ch

	def endElement(self, name):
		if name == self.toFind:
			print(trim(self.found))


def find_elements(name):
	handler = FindContent(name)
	parser = make_parser()
	parser.setContentHandler(handler)
	parser.parse(open('films.xml'))

if __name__ == "__main__":
	name = sys.argv[1]
	find_elements(name)

