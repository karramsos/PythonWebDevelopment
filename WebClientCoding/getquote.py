import urllib, re, sys

symbol = sys.argv[1] # Use module as: python getquote.py mmm
url = 'http://finance.google.com/finance?q='
content = urllib.urlopen(url+symbol).read()
m = re.search('span id="ref.*>(.*)<', content)
if m:
	quote = m.group(1)
else:
	quote = 'No quote for symbol: ' + symbol

print (quote)