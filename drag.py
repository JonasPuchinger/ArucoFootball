# code from https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets
# modified for this purpose and PyQt 5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

class ThumbListWidget(QListWidget):
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
            if item is not None and self.itemWidget(item) is None:
                index, name, icon = item.data(Qt.UserRole)
                widget = QCustomQWidget()
                widget.setTextUp(index)
                widget.setTextDown(name)
                widget.setIcon(icon)
                item.setSizeHint(widget.sizeHint())
                self.setItemWidget(item, widget)

    

class MainWindow(QMainWindow):
    def __init__(self, player_data):
        super(QMainWindow,self).__init__()
        self.listItems = {}
        myQWidget = QWidget()
        myBoxLayout = QHBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = ThumbListWidget(self)

        for player in player_data:
            player = (player.number, player.name, player.pic_path)
            myQListWidgetItem = QListWidgetItem(self.listWidgetA)
            # store the player needed to create/re-create the custom widget
            myQListWidgetItem.setData(Qt.UserRole, player)
            self.listWidgetA.addItem(myQListWidgetItem)

        self.listWidgetB = ThumbListWidget(self)
        myBoxLayout.addWidget(self.listWidgetB)
        myBoxLayout.addWidget(self.listWidgetA)

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
            color: rgb(255, 0, 0);
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
