#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtSql
import sys
      

def check_error(q):
    
    ler = q.lastError()

    if ler.isValid():
        print ler.text()        

def main():       
        
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("test.db")
    
    if not db.open():
        print "Cannot establish a database connection"
        sys.exit(1)
        
    q = QtSql.QSqlQuery()
    q.prepare("SELECT Name, Price FROM Cars WHERE Id = ?")
    q.bindValue(0, 6)
    q.exec_()
    check_error(q)

    q.first()

    name = q.value(0)
    price = q.value(1)
    print name, price

    db.close()

if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)