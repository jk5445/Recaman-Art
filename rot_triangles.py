from graphics import *
import math

class Triangle:
	def __init__(self, r, theta, step, rot, fill, outline, x, y, win):
		self.r = r
		self.theta = theta
		self.step = step
		self.rot = rot
		self.fill = fill
		self.outline = outline
		self.x = x
		self.y = y
		self.win = win
		self.triangle = Polygon()
		self.set()

	def update(self):
		self.undraw()
		self.expand()
		self.rotate()
		self.set()
		self.draw()

	def expand(self):
		self.r += self.step

	def rotate(self):
		self.theta += self.rot

	def set(self):
		x = self.x
		y = self.y
		r = self.r
		theta = self.theta
		p1 = Point(x + r*math.cos(theta), y - r*math.sin(theta))
		p2 = Point(x + r*math.cos(theta+2/3*math.pi), y - r*math.sin(theta+2/3*math.pi))
		p3 = Point(x + r*math.cos(theta+2*2/3*math.pi), y - r*math.sin(theta+2*2/3*math.pi))
		vertices = [p1, p2, p3]
		triangle = Polygon(vertices)
		self.triangle = triangle

	def undraw(self):
		self.triangle.undraw()

	def draw(self):
		self.triangle.setFill(self.fill)
		self.triangle.setOutline(self.outline)
		self.triangle.draw(self.win)

def main():
	win = GraphWin("Press q to quit", 400, 400, autoflush=False)
	win.setCoords(0, 0, win.getWidth(), win.getHeight())
	win.setBackground('magenta')

	triangles = []

	T = Triangle(100, 0, 1, 1/20, 'cyan', 'yellow', win.getWidth()/2, win.getHeight()/2, win)
	triangles.append(T)
	
	run = True
	while run:
		for T in triangles:
			T.update()
		update()
		if win.checkKey() == 'q':
			run = False

	win.close()

main()
