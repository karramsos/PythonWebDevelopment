#!/usr/bin/python
# -*- coding: utf -8 -*-

from PySide import QtCore, QtSql
import sys

def check_error(q):
    
    ler = q.lastError()
    
    if ler.isValid():
        print ler.text()

        
def main():
    
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("allsortsDB.db")
    
    if not db.open():
        print "Cannot establish a database connection"
        sys.exit(1)
        
    q = QtSql.QSqlQuery()
    q.exec_("delete from cars where id in (1,2,3)")
    check_error(q)
    
    print "The query affected %d rows" % q.numRowsAffected()
    
    db.close()
    
if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)
    