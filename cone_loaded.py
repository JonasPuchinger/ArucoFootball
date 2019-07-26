from OpenGL.GL import *
import pygame

def get_gl_list():

    mtl = {}
    surf = pygame.image.load('devil.jpg')
    image = pygame.image.tostring(surf, 'RGBA', 1)
    ix, iy = surf.get_rect().size
    texid = mtl['Material.001'] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)


    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([0.5, 1.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([0.597545, 0.990393])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([0.691342, 0.96194])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([0.777785, 0.915735])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([0.853553, 0.853553])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([0.915735, 0.777785])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([0.96194, 0.691342])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([0.990393, 0.597545])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([1.0, 0.5])
    glVertex3fv([1.6, 1.0, 0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([0.990393, 0.402455])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([0.96194, 0.308658])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([0.915735, 0.222215])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([0.853553, 0.146447])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([0.777785, 0.084265])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([0.691342, 0.03806])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([0.597545, 0.009607])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([0.5, 0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([0.402455, 0.009607])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([0.308658, 0.03806])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([0.222215, 0.084265])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([0.146446, 0.146447])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([0.084265, 0.222215])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([0.03806, 0.308659])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([0.009607, 0.402455])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([0.0, 0.5])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([0.009607, 0.597546])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([0.03806, 0.691342])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([0.084266, 0.777786])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([0.146447, 0.853554])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([0.222215, 0.915735])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([0.308659, 0.96194])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([0.402456, 0.990393])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glEnd()
    glEndList()

    return gl_listfrom OpenGL.GL import *
import pygame

def get_gl_list():

    mtl = {}
    surf = pygame.image.load('devil.jpg')
    image = pygame.image.tostring(surf, 'RGBA', 1)
    ix, iy = surf.get_rect().size
    texid = mtl['Material.001'] = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texid)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)


    gl_list = glGenLists(1)
    glNewList(gl_list, GL_COMPILE)
    glFrontFace(GL_CCW)
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.6, 1.0, 0.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([0.0, 0.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glVertex3fv([0.6, -1.0, -0.0])
    glTexCoord2fv([1.0, 0.0])
    glVertex3fv([0.6, -1.0, -0.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([1.0, 1.0])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glEnd()
    glColor(*mtl['Kd'])
    glBegin(GL_POLYGON)
    glVertex3fv([0.6, 1.0, 1.0])
    glTexCoord2fv([0.5, 1.0])
    glVertex3fv([0.6, 1.0, 1.0])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glTexCoord2fv([0.597545, 0.990393])
    glVertex3fv([0.79509, 1.0, 0.980785])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glTexCoord2fv([0.691342, 0.96194])
    glVertex3fv([0.982683, 1.0, 0.92388])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glTexCoord2fv([0.777785, 0.915735])
    glVertex3fv([1.15557, 1.0, 0.83147])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glTexCoord2fv([0.853553, 0.853553])
    glVertex3fv([1.307107, 1.0, 0.707107])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glTexCoord2fv([0.915735, 0.777785])
    glVertex3fv([1.43147, 1.0, 0.55557])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glTexCoord2fv([0.96194, 0.691342])
    glVertex3fv([1.52388, 1.0, 0.382684])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glTexCoord2fv([0.990393, 0.597545])
    glVertex3fv([1.580785, 1.0, 0.19509])
    glVertex3fv([1.6, 1.0, 0.0])
    glTexCoord2fv([1.0, 0.5])
    glVertex3fv([1.6, 1.0, 0.0])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glTexCoord2fv([0.990393, 0.402455])
    glVertex3fv([1.580785, 1.0, -0.19509])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glTexCoord2fv([0.96194, 0.308658])
    glVertex3fv([1.52388, 1.0, -0.382683])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glTexCoord2fv([0.915735, 0.222215])
    glVertex3fv([1.43147, 1.0, -0.55557])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glTexCoord2fv([0.853553, 0.146447])
    glVertex3fv([1.307107, 1.0, -0.707107])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glTexCoord2fv([0.777785, 0.084265])
    glVertex3fv([1.15557, 1.0, -0.83147])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glTexCoord2fv([0.691342, 0.03806])
    glVertex3fv([0.982683, 1.0, -0.92388])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glTexCoord2fv([0.597545, 0.009607])
    glVertex3fv([0.79509, 1.0, -0.980785])
    glVertex3fv([0.6, 1.0, -1.0])
    glTexCoord2fv([0.5, 0.0])
    glVertex3fv([0.6, 1.0, -1.0])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glTexCoord2fv([0.402455, 0.009607])
    glVertex3fv([0.404909, 1.0, -0.980785])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glTexCoord2fv([0.308658, 0.03806])
    glVertex3fv([0.217316, 1.0, -0.923879])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glTexCoord2fv([0.222215, 0.084265])
    glVertex3fv([0.044429, 1.0, -0.831469])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glTexCoord2fv([0.146446, 0.146447])
    glVertex3fv([-0.107107, 1.0, -0.707106])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glTexCoord2fv([0.084265, 0.222215])
    glVertex3fv([-0.23147, 1.0, -0.55557])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glTexCoord2fv([0.03806, 0.308659])
    glVertex3fv([-0.32388, 1.0, -0.382683])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glTexCoord2fv([0.009607, 0.402455])
    glVertex3fv([-0.380785, 1.0, -0.195089])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glTexCoord2fv([0.0, 0.5])
    glVertex3fv([-0.4, 1.0, 1e-06])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glTexCoord2fv([0.009607, 0.597546])
    glVertex3fv([-0.380785, 1.0, 0.195091])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glTexCoord2fv([0.03806, 0.691342])
    glVertex3fv([-0.323879, 1.0, 0.382685])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glTexCoord2fv([0.084266, 0.777786])
    glVertex3fv([-0.231469, 1.0, 0.555571])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glTexCoord2fv([0.146447, 0.853554])
    glVertex3fv([-0.107106, 1.0, 0.707108])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glTexCoord2fv([0.222215, 0.915735])
    glVertex3fv([0.044431, 1.0, 0.83147])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glTexCoord2fv([0.308659, 0.96194])
    glVertex3fv([0.217318, 1.0, 0.92388])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glTexCoord2fv([0.402456, 0.990393])
    glVertex3fv([0.404911, 1.0, 0.980786])
    glEnd()
    glEndList()

    return gl_list