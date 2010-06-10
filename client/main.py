from socket import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import gfx



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800,600)
glutCreateWindow("NetPaint on Python")
glClearColor(1.0,1.0,1.0,1.0)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0.0,800.0,0,600.0)
glutDisplayFunc(gfx.render)
glutMouseFunc(gfx.mouse)
glutMotionFunc(gfx.motion)
glutIdleFunc(gfx.idle)
glutMainLoop()
