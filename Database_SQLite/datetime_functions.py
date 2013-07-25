#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

a = lite.Time(14, 30, 33)
print a, type(a)

b = lite.Timestamp(2013, 5, 3, 16, 33, 10)
print b, type(b)

c = lite.TimeFromTicks(1360090360)
print c, type(c)

d = lite.TimestampFromTicks(1360090360)
print d, type(d)
