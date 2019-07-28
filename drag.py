# code from https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets
# modified for this purpose and PyQt 5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

# http://www.informit.com/articles/article.aspx?p=1187104&seqNum=3
class CommandAdd(QUndoCommand):
    def __init__(self, listWidget, row, item, itemWidget, description):
        super(CommandAdd, self).__init__(description)
        self.listWidget = listWidget
        self.row = row
        self.item = item
        self.itemWidget = itemWidget

    def redo(self):
        self.listWidget.setItemWidget(self.item, self.itemWidget)
        # self.listWidget.insertItem(self.row, self.item)
        # self.listWidget.setCurrentRow(self.row)

    def undo(self):
        pass
        # item = self.listWidget.takeItem(self.row)
        # del item

# class CommandRemove(QUndoCommand):
#     def __init__(self, listWidget, row, item, description):
#         super(CommandRemove, self).__init__(description)
#         self.listWidget = listWidget
#         self.item = item
#         self.row = row

#     def redo(self):
#         pass

#     def undo(self):
#         pass

class ThumbListWidget(QListWidget):

    playerAddedSignal = pyqtSignal(QListWidgetItem, QWidget, str)
    playerRemovedSignal = pyqtSignal(QListWidgetItem, str)

    def __init__(self, type, name, parent=None):
        super(ThumbListWidget, self).__init__(parent)
        self.setIconSize(QSize(124, 124))
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDefaultDropAction(Qt.MoveAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setAcceptDrops(True)
        self.instance_name = name
        self.model().rowsInserted.connect(
            self.handleRowsInserted, Qt.QueuedConnection)
        # self.model().rowsRemoved.connect(
        #     self.handleRowsRemoved, Qt.QueuedConnection)

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
                self.playerAddedSignal.emit(item, widget, self.instance_name)
    
    # def handleRowsRemoved(self, parent, first, last):
    #     for index in range(first, last + 1):
    #         item = self.item(index)
    #         if item is not None:
    #             self.playerRemovedSignal.emit(item, self.instance_name)

class MainWindow(QMainWindow):
    def __init__(self, player_data):
        super(QMainWindow,self).__init__()

        self.undoStack = QUndoStack()
        # self.createActions()

        self.listItems = {}

        myQWidget = QWidget()
        myBoxLayout = QHBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = ThumbListWidget(self, "listA")
        self.listWidgetA.playerAddedSignal.connect(self.playerAdded)
        # self.listWidgetA.playerRemovedSignal.connect(self.playerRemoved)

        for data in player_data:
            myQListWidgetItem = QListWidgetItem(self.listWidgetA)
            # store the data needed to create/re-create the custom widget
            myQListWidgetItem.setData(Qt.UserRole, data)
            self.listWidgetA.addItem(myQListWidgetItem)

        self.listWidgetB = ThumbListWidget(self, "listB")
        self.listWidgetB.playerAddedSignal.connect(self.playerAdded)
        # self.listWidgetB.playerRemovedSignal.connect(self.playerRemoved)

        myBoxLayout.addWidget(self.listWidgetB)
        myBoxLayout.addWidget(self.listWidgetA)

    # https://doc.qt.io/archives/qtjambi-4.5.2_01/com/trolltech/qt/qtjambi-undoframework.html
    def createActions(self):
        self.undoAction = QAction("&Undo", self)
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.undoStack.undo)
        
        self.redoAction = QAction("&Redo", self)
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.undoStack.redo)

    def playerAdded(self, item, widget, parent):
        command = None
        if parent == "listA":
            print("{} added in {}".format(item.data(Qt.UserRole)[1], parent))
            print("{} removed from listB".format(item.data(Qt.UserRole)[1], parent))
            command = CommandAdd(self.listWidgetA, self.listWidgetA.currentRow(), item, widget, "Add {}".format(item.data(Qt.UserRole)[1]))
        if parent == "listB":
            print("{} added in {}".format(item.data(Qt.UserRole)[1], parent))
            print("{} removed from listA".format(item.data(Qt.UserRole)[1], parent))
            command = CommandAdd(self.listWidgetB, self.listWidgetB.currentRow(), item, widget, "Add {}".format(item.data(Qt.UserRole)[1]))
        self.undoStack.push(command)

    # def playerRemoved(self, item, parent):
    #     print("{} removed from {}".format(item.data(Qt.UserRole)[1], parent))
    #     command = None
    #     if parent == "listA":
    #         command = CommandRemove(self.listWidgetA, self.listWidgetA.currentRow(), item, "Remove {}".format(item.data(Qt.UserRole)[1]))
    #     if parent == "listB":
    #         command = CommandRemove(self.listWidgetB, self.listWidgetB.currentRow(), item, "Remove {}".format(item.data(Qt.UserRole)[1]))
    #     self.undoStack.push(command)

    # TODO: swap player


class QCustomQWidget(QWidget):
    def __init__(self, parent=None):
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

    def setTextUp(self, text):
        self.textUpQLabel.setText(text)

    def setTextDown(self, text):
        self.textDownQLabel.setText(text)

    def setIcon(self, imagePath):
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToHeight(50)
        self.iconQLabel.setPixmap(pixmap)
