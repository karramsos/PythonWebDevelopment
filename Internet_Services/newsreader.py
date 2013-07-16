from nntplib import *

s = NNTP('web.aioe.org')
(resp, count, first, last, name) = s.group('comp.lang.python')
(resp, subs) = s.xhdr('subject', (str(first) + '-'+str(last)))
for subject in subs[-10:]:
	print(subject)
number = input('Which article do you want to read? ')
(reply, num, id, list) = s.body(str(number))
for line in list:
	print(line)