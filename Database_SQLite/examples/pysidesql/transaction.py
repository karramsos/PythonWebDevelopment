#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtSql
import sys      

def check_error(q, db):
    
    ler = q.lastError()

    if ler.isValid():
        print ler.text()  
        db.rollback()
        sys.exit(1)


def main():    

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    
    db.setDatabaseName("test.db")        

    if not db.open():
        print "cannot establish a database connection"
        sys.exit(1)

    db.transaction() 
    q = QtSql.QSqlQuery()
    q.exec_("DROP TABLE IF EXISTS Cars")
    check_error(q, db)
    q.exec_("CREATE TABLE Cars(Id INT," 
        "Name TEXT, Price INT)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(1,'Audi',52642)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(7,'Hummer',41400)")    
    check_error(q, db)
    q.exec_("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")  
    check_error(q, db)
    db.commit()

    db.close()

if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)
    
