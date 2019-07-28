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
import threading
 
class OpenGLGlyphs:
  
    # constants
    INVERSE_MATRIX = np.array([[ 1.0, 1.0, 1.0, 1.0],
                               [-1.0,-1.0,-1.0,-1.0],
                               [-1.0,-1.0,-1.0,-1.0],
                               [ 1.0, 1.0, 1.0, 1.0]])
 
    def __init__(self):
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
        self.set_players = []
 
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
        self.player3 = OBJ('football-player1.obj', 3)
        #self.player2 = OBJ('football-player2.obj')
        #self.player3 = OBJ('football-player3.obj')
        #self.player4 = OBJ('football-player4.obj')
        #self.player5 = OBJ('football-player5.obj')
        #self.player6 = OBJ('football-player6.obj')
        #self.player7 = OBJ('football-player7.obj')
        #self.player8 = OBJ('football-player8.obj')
        #self.player9 = OBJ('football-player9.obj')
        #self.player10 = OBJ('football-player10.obj')
        #self.player11 = OBJ('football-player11.obj')
        #self.player12 = OBJ('football-player12.obj')
        #self.player13 = OBJ('football-player13.obj')
        #self.player14 = OBJ('football-player14.obj')
        #self.player15 = OBJ('football-player15.obj')
        #self.player16 = OBJ('football-player16.obj')
        # self.cone = OBJ('cone.obj')
        # self.sphere = OBJ('sphere.obj')
 
        # assign texture
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)

    def initGUI(self):
        app = QApplication(sys.argv)
        player_data = [("1", "player1", "devil.jpg"), ("2", "player2", "devil.jpg")]
        self.mainWindow = MainWindow(player_data)
        self.mainWindow.show()
        self.set_player_widget = self.mainWindow.listWidgetB

        self.mainWindow.resize(800,800)
        app.exec_()
    
    def setChangedListItems(self):
        items = []
        for index in range(self.set_player_widget.count()):
            item = self.set_player_widget.item(index)
            if item:
                items.append(item.data(Qt.UserRole))
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
            rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 1, self.mtx, self.dist)
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
 
            if player_count < len(self.set_players):
                if glyph_name == 1:
                    glCallList(self.player1.gl_list)
                if glyph_name == 2:
                    glCallList(self.player2.gl_list)
                #glCallList(self.player2.gl_list)
                #glCallList(self.player3.gl_list)
                player_count += 1
 
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
openGLGlyphs = OpenGLGlyphs()
openGLGlyphs.main()
