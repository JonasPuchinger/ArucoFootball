from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
from PIL import Image
import numpy as np
from webcam import Webcam
from objloader import *
from aruco_detection import *
from drag import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from player import Player
import threading
import WiiModel


class ArucoFootball:

    # constants
    INVERSE_MATRIX = np.array([[1.0, 1.0, 1.0, 1.0],
                               [-1.0, -1.0, -1.0, -1.0],
                               [-1.0, -1.0, -1.0, -1.0],
                               [1.0, 1.0, 1.0, 1.0]])

    def __init__(self, btAddr):
        self.btAddr = btAddr
        # initialise shapes
        self.player = None
        # initialise texture
        self.texture_background = None
        # init player lists
        self.set_ids = []
        self.set_players = []
        self.players = []
        # init camera values
        self.calc_values()
        # initialise webcam and start thread
        self.webcam = Webcam()
        self.webcam.start()
        # connect wiimote and create model
        wiiModel = WiiModel.WiiModel(self.btAddr)
        # init openGl, Qt and Wiimote
        self.initOpenGL()
        self.initGUI()
        # run wiimote-connection-loop
        thread = threading.Thread(target=wiiModel.wiimoteLoop, args=(self.mainWindow, self.cursor))
        thread.start()
        # run opengl and camera in a thread
        thread = threading.Thread(target=glutMainLoop, args=())
        thread.start()
        # run Qt
        self.app.exec_()

    def initGUI(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = MainWindow(self.players)
        self.mainWindow.show()
        self.set_player_widget = self.mainWindow.listWidgetB
        self.unset_player_widget = self.mainWindow.listWidgetA

        self.unset_player_widget.itemChanged.connect(self.removeID)
        self.mainWindow.setFocus()
        self.mainWindow.setWindowTitle("Tactic-Window")
        self.mainWindow.resize(600, 800)
        self.cursor = QCursor()

    def initOpenGL(self):
        # setup OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(1280, 960)
        glutInitWindowPosition(800, 400)
        self.window_id = glutCreateWindow("Footballfield")
        glutDisplayFunc(self._draw_scene)
        glutIdleFunc(self._draw_scene)

        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(33.7, 1.3, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        # assign shapes
        self.player1 = OBJ('football-player-new.obj', 1)
        # self.player2 = OBJ('football-player-new.obj', 2)
        # self.player3 = OBJ('football-player-new.obj', 3)
        # self.player4 = OBJ('football-player-new.obj', 4)
        # self.player5 = OBJ('football-player1.obj', 5)
        # self.player6 = OBJ('football-player1.obj', 6)
        # self.player7 = OBJ('football-player1.obj', 7)

        # add Players to list
        self.players.append(Player("Dani", "1", "dani-img.jpg", self.player1))
        # self.players.append(Player("Maxi", "2", "maxi-img.jpg", self.player2))
        # self.players.append(Player("Jonas", "3", "jonas-img.jpg", self.player3))
        # self.players.append(Player("Michi", "4", "michi-img.jpg", self.player4))

        # assign texture
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)

    # player removed from list, remove set id
    def removeID(self):
        for index in range(self.unset_player_widget.count()):
            item = self.unset_player_widget.item(index)
            if item:
                data = item.data(Qt.UserRole)
                if data:
                    for player in self.players:
                        if player.number == data[0] and player.marker_num is not None:
                            self.set_ids.remove(player.marker_num)
                            player.marker_num = None

    # add players to set_players for all players on "Field"
    def setChangedListItems(self):
        items = []
        for index in range(self.set_player_widget.count()):
            item = self.set_player_widget.item(index)
            if item:
                data = item.data(Qt.UserRole)
                for player in self.players:
                    if player.number == data[0]:
                        items.append(player)

        self.set_players = items

    def _draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # get image from webcam
        image = self.webcam.get_current_frame()

        # convert image to OpenGL texture format
        bg_image = cv2.flip(image, 0)
        bg_image = Image.fromarray(bg_image)
        ix = bg_image.size[0]
        iy = bg_image.size[1]
        bg_image = bg_image.tobytes("raw", "BGRX", 0, -1)

        # create background texture
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, bg_image)

        # draw background
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glPushMatrix()
        glTranslatef(0.0, 0.0, -10.0)
        self._draw_background()
        glPopMatrix()

        # handle glyphs
        image = self._handle_aruco(image)

        glutSwapBuffers()

    def calc_values(self):
        path = 'calib_images/*.jpg'
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = Tracker.calculate_camera_values(path)

    def _handle_aruco(self, image):
        img = image
        corners, ids, _ = Tracker.preprocess(img)
        if np.all(ids is not None):
            # check for OpenCV output in different versions
            params = aruco.estimatePoseSingleMarkers(corners, 1, self.mtx, self.dist)
            if len(params) == 2:
                rvec, tvec = params
            else:
                rvec, tvec, _ = params
        else:
            return

        # set all players to list from "Field"
        self.setChangedListItems()
        for i in range(len(ids)):

            rvecs, tvecs, glyph_name = rvec[i], tvec[i], ids[i][0]
            # build view matrix
            rmtx = cv2.Rodrigues(rvecs)[0]

            view_matrix = np.array([[rmtx[0][0], rmtx[0][1], rmtx[0][2], tvecs[0][0]],
                                    [rmtx[1][0], rmtx[1][1], rmtx[1][2], tvecs[0][1]],
                                    [rmtx[2][0], rmtx[2][1], rmtx[2][2], tvecs[0][2]],
                                    [0.0, 0.0, 0.0, 1.0]])

            view_matrix = view_matrix * self.INVERSE_MATRIX

            view_matrix = np.transpose(view_matrix)

            # load view matrix and draw shape
            glPushMatrix()
            glLoadMatrixd(view_matrix)

            # check if ID is set or not and set it
            if ids[i] not in self.set_ids:
                for player in self.set_players:
                    if player.marker_num is None:
                        player.marker_num = ids[i]
                        self.set_ids.append(ids[i])
                        break

            # if ID is set project model
            for player in self.set_players:
                if player.marker_num == ids[i]:
                    glCallList(player.model.gl_list)

            glPopMatrix()

    def _draw_background(self):
        # draw background
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(4.0,  3.0, 0.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-4.0,  3.0, 0.0)
        glEnd()

if __name__ == "__main__":
    ArucoFootball = ArucoFootball(sys.argv[1])
