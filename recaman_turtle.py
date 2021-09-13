import turtle
import numpy as np

window = turtle.Screen()
window.colormode(255)

scale = 2

# Right Side
joe = turtle.Turtle()
joe.speed(0)

seen = set()
current = 0

for step in range(200):
    sign = 1
    c = np.random.randint(low=0, high=255, size = 3)
    joe.pencolor((c[0], c[1], c[2]))
    
    if current - step > 0 and current - step not in seen:
        sign = -1

    joe.setheading(-sign*90)
    joe.circle(scale*step/2, 180)

    current += sign*step
    seen.add(current)


# Left Side
joe = turtle.Turtle()
joe.speed(0)

seen.clear()
current = 0

for step in range(200):
    sign = 1
    c = np.random.randint(low=0, high=255, size = 3)
    joe.pencolor((c[0], c[1], c[2]))

    if current - step > 0 and current - step not in seen:
        sign = -1

    joe.setheading(sign*90)
    joe.circle(scale*step/2, -180)

    current += sign*step
    seen.add(current)

turtle.done()