from graphics import *
import math
from numpy import random

# A class for rotating triangles
class Triangle:
	def __init__(self, r, theta, step, rot, fill, outline, x, y, win):
		self.r = r #radius
		self.theta = theta #orientation
		self.step = step #radius growth speed
		self.rot = rot #rotation speed

		# Colors
		self.fill = fill
		self.outline = outline

		# Center of triangle
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
	win = GraphWin("Click to play. Press q to quit", 400, 400, autoflush=False)
	win.setCoords(0, 0, win.getWidth(), win.getHeight())
	win.setBackground('white')

	# Instanciate Triangle with random
	# radius, rotational speed and direction, and color
	def randomTriangle(x, y):
		r = 10 + (100-10) * random.random()
		rot = 1/40 + (1/40 - 1/10) * random.random()
		direction = random.random()
		if direction >= 1/2:
			rot = -rot

		c = random.randint(low=0, high=255, size=3)
		color = color_rgb(c[0], c[1], c[2])

		T = Triangle(r, 0, 1, rot, color, 'black', x, y, win)
		return T

	# Instanciate first Triangle
	triangles = []
	T = randomTriangle(win.getWidth()/2, win.getHeight()/2)
	triangles.append(T)
	
	run = True
	while run:
		# Create new Triangle instances
		mouse = win.checkMouse()
		if mouse:
			T = randomTriangle(mouse.x, mouse.y)
			triangles.append(T)

		# Update triangles
		for T in triangles:
			T.update()
			if T.r > max(win.getHeight(), win.getWidth()):
				T.undraw()
				triangles.remove(T)
		update()

		# Check to quit
		if win.checkKey() == 'q':
			run = False

	win.close()

main()
