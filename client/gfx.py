from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import net

buf = 1024

def drawDot(x,y):
	glPointSize(3)
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POINT)
	glVertex2i(x,600-y)
	glEnd()
	data = '%(X)d.%(Y)d' % {'X':x,'Y':y}
	if(net.CliSocket.sendto(data,net.SrvAddr)):
		print "Coordinates sent!"
	
def drawDotStatic(x,y):
	glPointSize(3)
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_POINT)
	glVertex2i(x,600-y)
	glEnd()

def mouse(button,state,x,y):
	if state==GLUT_DOWN:
		if button==GLUT_LEFT_BUTTON:
			drawDot(x,y)
			glFlush()
	

def motion(x,y):
	drawDot(x,y)
	glFlush()

def render():
	glClear(GL_COLOR_BUFFER_BIT)
	print "Im in render()"
	try:
		CliData,CliAddr = net.CliSocket.recvfrom(buf)
		stext = CliData.split(".")
		x = int(stext[0])
		y = int(stext[1])
		drawDotStatic(x,y)
		rdata = 'Got: %(X)d.%(Y)d' % {'X':x,'Y':y}
		print rdata
	except:
		print "Got Nothing!"
		pass
	glFlush()
	
def idle():
	glutSwapBuffers()
	while(1):
		CliData,CliAddr = net.CliSocket.recvfrom(buf)
		stext = CliData.split(".")
		x = int(stext[0])
		y = int(stext[1])
		drawDotStatic(x,y)
		rdata = 'Got: %(X)d.%(Y)d' % {'X':x,'Y':y}
		print rdata
		glutSwapBuffers()
