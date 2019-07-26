import pygame
from OpenGL.GL import *
from os import path
import importlib

# https://rdmilligan.wordpress.com/2015/11/30/blender-animation-in-opengl-mark-ii/

def init_file(filename):
    l_f = "{}_loaded.py".format(filename.split(".")[0])

    with open(l_f, "a") as loaded_file:
        loaded_file.write("from OpenGL.GL import *\n")
        loaded_file.write("import pygame\n\n")
        loaded_file.write("def get_gl_list():\n\n")
        loaded_file.write("    mtl = {}\n")

def write_value(value, number_of_indents, filename):
    l_f = "{}_loaded.py".format(filename.split(".")[0])
 
    for _ in range(number_of_indents):
        value = '    ' + value
 
    value += '\n'
 
    with open(l_f, "a") as loaded_file:
        loaded_file.write(value)

def finish_file(filename):
    l_f = "{}_loaded.py".format(filename.split(".")[0])

    with open(l_f, "a") as loaded_file:
        loaded_file.write("\n")
        loaded_file.write("    return gl_list")

    print("Finished caching {}".format(l_f))

def MTL(filename):
    init_file(filename)
    contents = {}
    mtl = None
    for line in open(filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
            currMtlName = values[1]
        elif mtl is None:
            raise ValueError("mtl file doesn't start with newmtl stmt")
        elif values[0] == 'map_d':
            pass
        elif values[0] == 'map_Ks':
            pass
        elif values[0] == 'map_Bump':
            pass
        elif values[0] == 'map_Kd':
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(mtl['map_Kd'])
            write_value('surf = pygame.image.load(\'{}\')'.format(mtl['map_Kd']), 1, filename)
            image = pygame.image.tostring(surf, 'RGBA', 1)
            write_value('image = pygame.image.tostring(surf, \'RGBA\', 1)', 1, filename)
            ix, iy = surf.get_rect().size
            write_value('ix, iy = surf.get_rect().size', 1, filename)
            texid = mtl[currMtlName] = glGenTextures(1)
            write_value('texid = mtl[\'{}\'] = glGenTextures(1)'.format(currMtlName), 1, filename)
            glBindTexture(GL_TEXTURE_2D, texid)
            write_value('glBindTexture(GL_TEXTURE_2D, texid)', 1, filename)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                GL_LINEAR)
            write_value('glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)', 1, filename)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            write_value('glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)', 1, filename)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
            write_value('glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)\n\n', 1, filename)
        else:
            mtl[values[0]] = list(map(float, values[1:]))
    return contents

class OBJ:
    def __init__(self, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = list(map(float, values[1:4]))
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append(list(map(float, values[1:3])))
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                self.mtl = MTL(values[1])
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

        self.gl_list = glGenLists(1)
        write_value('gl_list = glGenLists(1)', 1, filename)
        glNewList(self.gl_list, GL_COMPILE)
        write_value('glNewList(gl_list, GL_COMPILE)', 1, filename)
        # glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        write_value('glFrontFace(GL_CCW)', 1, filename)
        for face in self.faces:
            vertices, normals, texture_coords, material = face

            mtl = None
            if self.mtl and material:
                mtl = self.mtl[material]
                if 'texture_Kd' in mtl:
                    # use diffuse texmap
                    # glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
                    # write_value('glBindTexture(GL_TEXTURE_2D, mtl[\'texture_Kd\'])', 1, filename)
                    glBindTexture(GL_TEXTURE_2D, mtl[material])
                    write_value('glBindTexture(GL_TEXTURE_2D, mtl[\'{}\'])'.format(material), 1, filename)
                else:
                    # just use diffuse colour
                    glColor(*mtl['Kd'])
                    write_value('glColor(*mtl[\'Kd\'])', 1, filename)

            glBegin(GL_POLYGON)
            write_value('glBegin(GL_POLYGON)', 1, filename)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                    write_value('glVertex3fv({})'.format(self.vertices[vertices[i] - 1]), 1, filename)
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                    write_value('glTexCoord2fv({})'.format(self.texcoords[texture_coords[i] - 1]), 1, filename)
                glVertex3fv(self.vertices[vertices[i] - 1])
                write_value('glVertex3fv({})'.format(self.vertices[vertices[i] - 1]), 1, filename)
            glEnd()
            write_value('glEnd()', 1, filename)
        # glDisable(GL_TEXTURE_2D)
        glEndList()
        write_value('glEndList()', 1, filename)
        finish_file(filename)