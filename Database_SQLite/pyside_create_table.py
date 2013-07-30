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
    q.exec_("Drop table if exists Cars")
    check_error(q)
    q.exec_("create table Cars(Id Int, Name text, Price int)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(1,'Audi ',52642)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(2,'Mercedes ',57127)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(3,'Skoda ',9000)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(4,'Volvo ',29000)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(5,'Bentley ' ,350000)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(6,'Citroen ',21000)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(7,'Hummer ',41400)")
    check_error(q)
    q.exec_("INSERT INTO Cars VALUES(8,'Volkswagen ',21600)")
    check_error(q)
    
    db.close()

if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)

