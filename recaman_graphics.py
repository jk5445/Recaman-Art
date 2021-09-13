from graphics import GraphWin, update, Circle, Point
import sys
import tkinter

outline = 'antiquewhite1'
background = 'lightskyblue'

user_outline = ''
user_background = ''
argv = sys.argv[1:]

# Read command line arguments
for i in range(len(argv) - 1):
	if argv[i] in ("-o", "--outline"):
		user_outline = argv[i+1]
	if argv[i] in ("-b", "--background"):
		user_background = argv[i+1]

	if argv[i] in ("-h", "--Help"):
		print("Usage: recaman_graphics.py --outline=<outlinecolor> --background=<backgroundcolor>")
		print("Default colors are outline = antiquewhite1 and background = lightskyblue")

if len(argv) and argv[-1] in ("-h", "--Help"):
	print("Usage: recaman_graphics.py --outline=<outlinecolor> --background=<backgroundcolor>")
	print("Default colors are outline = antiquewhite1 and background = lightskyblue")

# Instanciate GraphWin
win = GraphWin("Recamán – Click Anywhere to Close", 1400, 800, autoflush=False)
win.setCoords(-win.getWidth()/2,-win.getHeight()/2,win.getWidth()/2,win.getHeight()/2)

# Test user input for validity
if user_outline:
	try:
		win.setBackground(user_outline)
		outline = user_outline
	except tkinter.TclError:
		print("Outline: " + user_outline + " is not a valid color name. Please enter a valid X11 color name.")
if user_background:
	try:
		win.setBackground(user_background)
		background = user_background
	except tkinter.TclError:
		print("Backround: " + user_background + " is not a valid color name. Please enter a valid X11 color name.")
print("Rendering with", outline, "outline and", background, "background")

# Render
win.setBackground(background)

seen = set()
current = 0

scale = 2

for step in range (500):
	sign = 1

	# Determine direction
	if current - step > 0 and current - step not in seen:
		sign = -1

	# Right side
	c = Circle(Point(scale*(2*current+sign*step)/2 , 0), scale*step/2)
	c.setOutline(outline)
	c.draw(win)

	# Left side
	c = Circle(Point(-scale*(2*current+sign*step)/2 , 0), scale*step/2)
	c.setOutline(outline)
	c.draw(win)

	# Update current
	current += sign*step
	seen.add(current)

update()

win.getMouse()
win.close()

print("Window closed")