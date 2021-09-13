from graphics import GraphWin, update, Circle, Point

win = GraphWin("Recamán – Click Anywhere to Close", 1400, 800, autoflush=False)
win.setCoords(-win.getWidth()/2,-win.getHeight()/2,win.getWidth()/2,win.getHeight()/2)

seen = set()
current = 0

scale = 2

for step in range (500):
	sign = 1

	#determine direction
	if current - step > 0 and current - step not in seen:
		sign = -1

	#right side
	c = Circle(Point(scale*(2*current+sign*step)/2 , 0), scale*step/2)
	c.draw(win)

	#left side
	c = Circle(Point(-scale*(2*current+sign*step)/2 , 0), scale*step/2)
	c.draw(win)

	#update current
	current += sign*step
	seen.add(current)

update()

win.getMouse()
win.close()