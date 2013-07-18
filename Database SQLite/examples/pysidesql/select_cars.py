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
    q.exec_("SELECT * FROM Cars LIMIT 5")
    check_error(q)

    while q.next():
        
        cid = q.value(0)
        name = q.value(1)
        price = q.value(2)
        
        print cid, name, price
        
    db.close()    

if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)