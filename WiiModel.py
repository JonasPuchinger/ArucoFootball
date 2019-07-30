import wiimote
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, Qt
from ProjectiveTransformation import ProjectiveTransformation as pt
import pyautogui
import time


class WiiModel:

    def __init__(self, btAddr):
        self.connectingWiimote(btAddr)
        self.transformation = pt()

    def connectingWiimote(self, btAddr):
        addr = btAddr
        name = None
        self.wm = wiimote.connect(addr, name)

    def wiimoteLoop(self, mainWindow, cursor):
        drawing_points = []
        button_pressed = False
        while True:
            QtGui.QGuiApplication.processEvents()
            if self.wm.buttons["A"]:
                if not button_pressed:
                    pyautogui.mouseDown(button='right')
                    button_pressed = not button_pressed
                else:
                    pyautogui.mouseUp(button='right')
                    button_pressed = not button_pressed
            if self.wm.buttons["Left"]:
                mainWindow.undoMethod(True)
            if self.wm.buttons["Right"]:
                mainWindow.undoMethod(False)

            state = self.wm.ir.get_state()
            if len(state) == 4:

                scoords = self.transformation.getLightPositions(state)
                point = self.transformation.getActualCoordinates(scoords)
                point = (point[0], 800-point[1])

                point = QPoint(int(point[0]), int(point[1]))
                cursor.setPos(mainWindow.mapFromGlobal(point))
                cursor.setShape(Qt.OpenHandCursor)
                mainWindow.setCursor(cursor)

            time.sleep(0.1)
