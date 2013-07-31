#!/usr/bin/python
# -*- coding: utf -8 -*-

from PySide import QtCore, QtSql
import sys

def check_error(q):
    
    ler = q.lastError()
    
    if ler.isValid():
        print ler.text()
        exit(1)
        
def main():
    
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    
    db.setDatabaseName("allsortsDB.db")
    
    if not db.open():
        print "Cannot establish a database connection"
        sys.exit(1)
        
    q = QtSql.QSqlQuery()
    q.exec_("select * from Cars limit 1")
    
    rec = q.record()
    
    print "Number of columns:", rec.count()
    
    print rec.fieldName(0)
    print rec.fieldName(1)
    print rec.fieldName(2)

if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)
