# code from https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets
# modified for this purpose and PyQt 5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os
import queue
import threading

class ThumbListWidget(QListWidget):

    playerAddedSignal = pyqtSignal()


    def __init__(self, type, parent=None):
        super(ThumbListWidget, self).__init__(parent)
        self.setIconSize(QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.model().rowsInserted.connect(
            self.handleRowsInserted, Qt.QueuedConnection)

    def handleRowsInserted(self, parent, first, last):
        for index in range(first, last + 1):
            item = self.item(index)
            if item: 
                if self.itemWidget(item) is None:
                    if item.data(Qt.UserRole): 
                        index, name, icon = item.data(Qt.UserRole)
                        widget = QCustomQWidget()
                        widget.setTextUp(index)
                        widget.setTextDown(name)
                        widget.setIcon(icon)
                        item.setSizeHint(widget.sizeHint())
                        self.setItemWidget(item, widget)
                        self.playerAddedSignal.emit()
    

class MainWindow(QMainWindow):
    def __init__(self, player_data):
        super(QMainWindow,self).__init__()
        self.createActions()
        self.player_data = player_data
        self.listItems = {}
        self.initialSettings = True
        self.initialCount = 0
        self.allItems = []
        self.listCount = 0
        self.setStyleSheet("font: Times New Roman")
        benchLabel = QLabel()
        benchLabel.setText("Bench: ")
        benchLabel.setStyleSheet("font: 30pt Times New Roman")
        fieldLabel = QLabel()
        fieldLabel.setText("Field: ")
        fieldLabel.setStyleSheet("font: 30pt Times New Roman")
        labelLayout = QHBoxLayout()
        labelLayout.addWidget(fieldLabel)
        labelLayout.addWidget(benchLabel)

        listLayout = QHBoxLayout()

        myQWidget = QWidget()
        myBoxLayout = QVBoxLayout()

        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = ThumbListWidget(self)
        self.listWidgetA.playerAddedSignal.connect(self.changedList)
        self.listWidgetA.setStyleSheet("background-color: #E5A574")
        for player in player_data:
            player = (player.number, player.name, player.pic_path)
            myQListWidgetItem = QListWidgetItem(self.listWidgetA)
            # store the player needed to create/re-create the custom widget
            myQListWidgetItem.setData(Qt.UserRole, player)
            self.listWidgetA.addItem(myQListWidgetItem)

        self.listWidgetB = ThumbListWidget(self)
        self.listWidgetB.setStyleSheet("background-color: #74E596")
        self.listWidgetB.playerAddedSignal.connect(self.changedList)
        listLayout.addWidget(self.listWidgetB)
        listLayout.addWidget(self.listWidgetA)

        myBoxLayout.addLayout(labelLayout)
        myBoxLayout.addLayout(listLayout)

        self.undo_count = -1
        self.undo_items = []


    def undoMethod(self, undo):        
        #self.allItems.append(self.undo_items)
        #self.undo_items = self.undo_items[:self.undo_count+1]
        if undo:
            if self.undo_count >= 1: 
                self.undo_count -= 1
                self.removeItems()
                self.addItems(self.undo_items[self.undo_count])
                #self.listCount += 1
                
        else:
           
            if self.undo_count < len(self.undo_items)-1:
                self.undo_count += 1
                self.removeItems()
                self.addItems(self.undo_items[self.undo_count])

            
    # https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/qtjambi-undoframework.html
    def createActions(self):
        self.undoAction = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.undoAction.activated.connect(lambda: self.undoMethod(True))
        

        self.redoAction = QShortcut(QKeySequence("Ctrl+Y"), self)
        self.redoAction.activated.connect(lambda: self.undoMethod(False))
        

    def removeItems(self):
        for widgets in (self.listWidgetA, self.listWidgetB):
            widgets.clear()


    def addItems(self, widgetList):
        items = []
        count = 0
        for listI in widgetList:
            for index in range(len(listI)):
                item = listI[index]
                if item:
                    if count == 0:
                        myQListWidgetItem = QListWidgetItem(self.listWidgetA)
                        myQListWidgetItem.setData(Qt.UserRole, item)
                        self.listWidgetA.addItem(myQListWidgetItem)
                    elif count == 1:
                        myQListWidgetItem = QListWidgetItem(self.listWidgetB)
                        myQListWidgetItem.setData(Qt.UserRole, item)
                        self.listWidgetB.addItem(myQListWidgetItem)
            count += 1
        self.initialCount -= len(self.player_data)

                        
    def changedList(self):
        if self.initialCount < len(self.player_data)-1:
            self.initialCount += 1

        else:
            self.undo_count += 1
            widgets = ()
            for listWidget in (self.listWidgetA, self.listWidgetB):
                saveWidget = []
                for index in range(listWidget.count()):
                    item = listWidget.item(index)
                    if item:
                        data = item.data(Qt.UserRole)
                        saveWidget.append(data)
                widgets += (saveWidget, )
            self.undo_items.append(widgets)
        

class QCustomQWidget (QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QHBoxLayout()
        self.iconQLabel      = QLabel()
        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)
        
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(0, 0, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(0, 0, 0);
        ''')

    def setTextUp (self, text):
        text = "Number: \n" + text
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        text = "Name: \n" +text
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToHeight(80)
        self.iconQLabel.setPixmap(pixmap)
