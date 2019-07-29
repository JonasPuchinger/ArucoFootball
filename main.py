from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
from PIL import Image
import numpy as np
from webcam import Webcam
from objloader import *
# from objloader_cache import *
from constants import *
from aruco_detection import *
import glob
from drag import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from player import Player
import threading
import wiimote
from ProjectiveTransformation import ProjectiveTransformation as pt
import time
import pyautogui

class OpenGLGlyphs:

    # constants
    INVERSE_MATRIX = np.array([[ 1.0, 1.0, 1.0, 1.0],
                               [-1.0,-1.0,-1.0,-1.0],
                               [-1.0,-1.0,-1.0,-1.0],
                               [ 1.0, 1.0, 1.0, 1.0]])

    def __init__(self, btAddr):
        # initialise webcam and start thread
        self.webcam = Webcam()
        self.webcam.start()
        # initialise shapes
        self.player = None
        self.cone = None
        self.sphere = None

        # initialise texture
        self.texture_background = None

        #init camera values
        self.calc_values()

        # init player lists
        self.set_ids = []
        self.set_players = []
        self.players = []

        # connect wiimote
        self.connectingWiimote(btAddr)
        self.transformation = pt()
        
    def connectingWiimote(self, btAddr):
        addr = btAddr
        name = None
        self.wm = wiimote.connect(addr, name)

    def getScoords(self, state):
        # bubblesort from: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
        n = len(state)
        for i in range(n):
            for j in range(0, n-i-1):
                if state[j]['x'] > state[j+1]['x']:
                    state[j], state[j+1] = state[j+1], state[j]

        # start points from top left corner counter-clockwise
        if state[0]['y'] < state[1]['y']:
            state[0], state[1] = state[1], state[0]

        if state[2]['y'] > state[3]['y']:
            state[2], state[3] = state[3], state[2]

        A = (state[0]['x'], state[0]['y'])
        B = (state[1]['x'], state[1]['y'])
        C = (state[2]['x'], state[2]['y'])
        D = (state[3]['x'], state[3]['y'])
        
        scoords = [A, B, C, D]
        return scoords

    def gameModel(self):
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

                print("A pushed...")
                #TODO start drag and drop
            state = self.wm.ir.get_state()
            if len(state) == 4:

                scoords = self.getScoords(state)
                point = self.transformation.getActualCoordinates(scoords)
                point = (point[0], 800-point[1])

                # check if calculated point is range of DrawableObject
                
                point = QPoint(int(point[0]), int(point[1]))
                self.cursor.setPos(self.mainWindow.mapFromGlobal(point))
                self.cursor.setShape(Qt.OpenHandCursor)
                self.mainWindow.setCursor(self.cursor)
            else:
                drawing_points = []

            time.sleep(0.1)


    def _init_gl(self, Width, Height):
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
        #self.player = OBJ('football-player.obj')
        self.player1 = OBJ('football-player1.obj', 1)
        self.player2 = OBJ('football-player1.obj', 2)
        #self.player3 = OBJ('football-player1.obj', 3)
        #self.player4 = OBJ('football-player1.obj', 4)
        #self.player5 = OBJ('football-player1.obj', 5)
        #self.player6 = OBJ('football-player1.obj', 6)
        #self.player7 = OBJ('football-player1.obj', 7)
        # self.cone = OBJ('cone.obj')
        # self.sphere = OBJ('sphere.obj')

        #add Players to list
        self.players.append(Player("Oliver Kahn", "1", "devil.jpg", self.player1))
        self.players.append(Player("Cristiano Ronaldo", "7", "devil.jpg", self.player2))
        
        # assign texture
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)

    def initGUI(self):
        app = QApplication(sys.argv)
        self.mainWindow = MainWindow(self.players)
        self.mainWindow.show()
        self.set_player_widget = self.mainWindow.listWidgetB
        self.unset_player_widget = self.mainWindow.listWidgetA
        self.unset_player_widget.itemChanged.connect(self.removeID)
        self.mainWindow.setFocus()
        self.mainWindow.resize(800,800)
        self.cursor = QCursor()
       
        thread = threading.Thread( target = self.gameModel ,args =())
        thread.start()

        app.exec_()

    def removeID(self):
        for index in range(self.unset_player_widget.count()):
            item = self.unset_player_widget.item(index)
            if item:
                data = item.data(Qt.UserRole)
                if data:
                    for player in self.players:
                        if player.number == data[0] and player.marker_num != None:
                            self.set_ids.remove(player.marker_num)
                            player.marker_num = None

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
        glTranslatef(0.0,0.0,-10.0)
        self._draw_background()
        glPopMatrix()

        # handle glyphs
        image = self._handle_glyphs(image)

        glutSwapBuffers()

    def calc_values(self):
        path = 'calib_images/*.jpg'
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = Tracker.calculate_camera_values(path)

    def _handle_glyphs(self, image):

        img = image
        corners, ids, _ = Tracker.preprocess(img)
        if np.all(ids != None):
            rvec, tvec = aruco.estimatePoseSingleMarkers(corners, 1, self.mtx, self.dist)
        else:
            return

        ######################################
        # attempt to detect glyphs
        glyphs = []

        player_count = 0
        self.setChangedListItems()
        for i in range(len(ids)):

            rvecs, tvecs, glyph_name = rvec[i], tvec[i], ids[i][0]
            # build view matrix

            rmtx = cv2.Rodrigues(rvecs)[0]

            view_matrix = np.array([[rmtx[0][0],rmtx[0][1],rmtx[0][2],tvecs[0][0]],
                                    [rmtx[1][0],rmtx[1][1],rmtx[1][2],tvecs[0][1]],
                                    [rmtx[2][0],rmtx[2][1],rmtx[2][2],tvecs[0][2]],
                                    [0.0       ,0.0       ,0.0       ,1.0    ]])

            view_matrix = view_matrix * self.INVERSE_MATRIX

            view_matrix = np.transpose(view_matrix)

            # load view matrix and draw shape
            glPushMatrix()
            glLoadMatrixd(view_matrix)
 
            if ids[i] not in self.set_ids:
                for player in self.set_players:
                    if player.marker_num is None:
                        player.marker_num = ids[i]
                        self.set_ids.append(ids[i])
                        break

            for player in self.set_players:
                if player.marker_num == ids[i]:
                    glCallList(player.model.gl_list)

            glPopMatrix()

    def _draw_background(self):
        # draw background
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0); glVertex3f(-4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 1.0); glVertex3f( 4.0, -3.0, 0.0)
        glTexCoord2f(1.0, 0.0); glVertex3f( 4.0,  3.0, 0.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(-4.0,  3.0, 0.0)
        glEnd( )

    def main(self):
        # setup and run OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(800, 400)
        self.window_id = glutCreateWindow("OpenGL Glyphs")
        glutDisplayFunc(self._draw_scene)
        glutIdleFunc(self._draw_scene)
        self._init_gl(640, 480)
       # run opengl and camera in a thread
        thread = threading.Thread( target = glutMainLoop ,args =())
        thread.start()
        # init GUI
        # PyQt needs MainThread to run
        self.initGUI()

# run an instance of OpenGL Glyphs

openGLGlyphs = OpenGLGlyphs(sys.argv[1])
openGLGlyphs.main()
