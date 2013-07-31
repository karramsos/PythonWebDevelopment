#!/usr/bin/python
# -*- coding: utf -8 -*-

from PySide import QtGui, QtCore, QtSql

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        
        super(Example, self).__init__()
        
        self.setGeometry(300, 300, 400, 330)
        self.setWindowTitle("Editable model")
        
        self.createConnection()
        self.createModel()
        self.initUI()
        
        self.statusBar().showMessage("Ready")
        
    def onClicked(self, index):
        
        self.statusBar().showMessage(str(index.data()))
        
    def createConnection(self):
        
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("allsortsDB.db")
        
        if not db.open():
            print "Cannot establish a database connection"
            return False
    
    def createModel(self):
        
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("Cars")
        self.model.select()
        
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, "Id")
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, "Name")
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Price")
        
        strategy = QtSql.QSqlTableModel.OnFieldChange
        self.model.setEditStrategy(strategy)
        
    def initUI(self):
        
        self.view = QtGui.QTableView()
        self.view.setModel(self.model)
        
        mode = QtGui.QAbstractItemView.SingleSelection
        self.view.setSelectionMode(mode)
        
        self.connect(self.view, QtCore.SIGNAL('clicked(QModelIndex)'), self.onClicked)
        self.setCentralWidget(self.view)
        
def main():
    
    app = QtGui.QApplication([])
    ex = Example()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()

    
    
    
    
    
