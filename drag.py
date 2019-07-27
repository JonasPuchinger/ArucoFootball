# code from https://stackoverflow.com/questions/41595014/dragndrop-custom-widget-items-between-qlistwidgets
# modified for this purpose and PyQt 5

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys, os

# http://www.informit.com/articles/article.aspx?p=1187104&seqNum=3
class CommandAdd(QUndoCommand):
    def __init__(self, listWidget, row, string, description):
        super(CommandAdd, self).__init__(description)
        self.listWidget = listWidget
        self.row = row
        self.string = string

    def redo(self):
        self.listWidget.insertItem(self.row, self.string)
        self.listWidget.setCurrentRow(self.row)

    def undo(self):
        item = self.listWidget.takeItem(self.row)
        del item

class ThumbListWidget(QListWidget):

    playerAddedSignal = pyqtSignal(str, str)

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
                self.playerAddedSignal.emit(name, str(parent))

class MainWindow(QMainWindow):
    def __init__(self, player_data):
        super(QMainWindow,self).__init__()

        self.undoStack = QUndoStack()

        self.listItems = {}

        myQWidget = QWidget()
        myBoxLayout = QHBoxLayout()
        myQWidget.setLayout(myBoxLayout)
        self.setCentralWidget(myQWidget)

        self.listWidgetA = ThumbListWidget(self)
        self.listWidgetA.playerAddedSignal.connect(self.playerAdded)

        for data in player_data:
            myQListWidgetItem = QListWidgetItem(self.listWidgetA)
            # store the data needed to create/re-create the custom widget
            myQListWidgetItem.setData(Qt.UserRole, data)
            self.listWidgetA.addItem(myQListWidgetItem)

        self.listWidgetB = ThumbListWidget(self)
        self.listWidgetB.playerAddedSignal.connect(self.playerAdded)

        myBoxLayout.addWidget(self.listWidgetB)
        myBoxLayout.addWidget(self.listWidgetA)

    def playerAdded(self, name, parent):
        print("{} added in {}".format(name, parent))
        # self.undoStack.push()


class QCustomQWidget(QWidget):
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
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        pixmap = QPixmap(imagePath)
        pixmap = pixmap.scaledToHeight(50)
        self.iconQLabel.setPixmap(pixmap)
