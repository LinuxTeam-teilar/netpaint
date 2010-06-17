from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import string
import dbus
import net

buf = 1024
c_r = 0.0
c_g = 0.0
c_b = 0.0
c_s = 2

renderTree = []
netTree = []

session_bus = dbus.SessionBus()

def drawDot(x,y):
	global c_r,c_g,c_b
	glColor3f(c_r,c_g,c_b)
	glPointSize(3)
	glBegin(GL_POINT)
	glVertex2i(x,600-y)
	glEnd()
	data = '%(X)d.%(Y)d.%(1)f.%(2)f.%(3)f' % {'X':x,'Y':y,'1':c_r,'2':c_g,'3':c_b}
	if(net.CliSocket.sendto(data,net.SrvAddr)):
		print "Data sent!"
	
def drawDotStatic(x,y,tr,tg,tb):
	glColor3f(tr,tg,tb)
	glPointSize(3)
	glBegin(GL_POINT)
	glVertex2i(x,600-y)
	glEnd()

def mouse(button,state,x,y):
	global netTree,c_r,c_g,c_b
	if state==GLUT_DOWN:
		if button==GLUT_LEFT_BUTTON:
			drawDotStatic(x,y,c_r,c_g,c_b)
			glFlush()
	elif state==GLUT_UP:
		data = str(netTree)
		if net.CliSocket.sendto(data,net.SrvAddr)>0:
			print "Sent data to server!"
			netTree=[]
	

def motion(x,y):
	global renderTree,netTree,c_r,c_g,c_b,c_s
	drawDotStatic(x,y,c_r,c_g,c_b)
	if [x,y,c_r,c_g,c_b] not in renderTree or netTree:
		netTree.append([x,y,c_r,c_g,c_b,c_s])
		renderTree.append([x,y,c_r,c_g,c_b,c_s])
	glFlush()
	

def renderRenderTree():
	global renderTree
	for p in renderTree:
		glColor3f(p[2],p[3],p[4])
		glPointSize(p[5]+1)
		glBegin(GL_POINT)
		glVertex2i(p[0],600-p[1])
		glEnd()


def keyb(k,x,y):
	global c_r,c_g,c_b,c_s
	if k=="1":
		c_r = c_r + 0.1
	elif k=="2":
		c_g = c_g + 0.1
	elif k=="3":
		c_b = c_b + 0.1
	elif k=="q":
		c_r = c_r - 0.1
	elif k=="w":
		c_g = c_g - 0.1
	elif k=="e":
		c_b = c_b - 0.1
	elif k=="4":
		c_s = c_s + 1
	elif k=="r":
		c_s = c_s - 1

def render():
	glClear(GL_COLOR_BUFFER_BIT)
	print "Im in render()"
	renderRenderTree()
	glFlush()
	
def idle():
	#x = int(stext[0])
	#y = int(stext[1])
	#tr = float(stext[2])
	#tg = float(stext[3])
	#tb = float(stext[4])
	#drawDotStatic(x,y,tr,tg,tb)
	#rdata = 'Got: %(X)d.%(Y)d.%(1)f.%(2)f.%(3)f' % {'X':x,'Y':y,'1':tr,'2':tg,'3':tb}
	#print rdata
	glutSwapBuffers()
