#!/usr/bin/python
# -*- coding: utf -8 -*-

from PySide import QtCore, QtSql
import sys

def main():
    
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    
    driver = db.driver()
    print driver.hasFeature(QtSql.QSqlDriver.Transactions)
    print driver.hasFeature(QtSql.QSqlDriver.BLOB)
    print driver.hasFeature(QtSql.QSqlDriver.Unicode)
    print "**********"
    print driver.hasFeature(QtSql.QSqlDriver.PreparedQueries)
    print driver.hasFeature(QtSql.QSqlDriver.NamedPlaceholders)
    print driver.hasFeature(QtSql.QSqlDriver.MultipleResultSets)
    print "**********"
    print driver.hasFeature(QtSql.QSqlDriver.QuerySize)
    print driver.hasFeature(QtSql.QSqlDriver.BatchOperations)
    print driver.hasFeature(QtSql.QSqlDriver.EventNotifications)
    
    db.close()
    
if __name__ == '__main__':
    
    app = QtCore.QCoreApplication([])
    main()
    sys.exit(0)
