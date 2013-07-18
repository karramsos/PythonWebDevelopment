#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtSql
import sys
      
      
def check_error(q):
    
    ler = q.lastError()

    if ler.isValid():
        print ler.text()      
        sys.exit(1)
    

def main():

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(":memory:")
    
    if not db.open():
        print "Cannot establish a database connection"
        sys.exit(1)

    q = QtSql.QSqlQuery()
    q.exec_("SELECT sqlite_version()")
    check_error(q)

    q.first()

    print q.value(0)

    db.close()


if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)





