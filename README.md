# Python Art
In this project I will introduce myself to some Python graphics tools using the recaman sequence. Hello world of mathematical art!

There are three python files in this repository (in order of my preference): recaman_graphics.py, rot_triangles.py, and recaman_turtle. Each can be run as is with no necessary command line arguments. recaman_graphics.py takes optional arguments. While rot_triangles.py is not based on the recaman sequence, it belongs in this repository of my cool Python graphic creations.

## Recaman Sequence
The recaman sequence is a defined by a recurrence relation that begins at 0. a[n] = a[n-1] - n if a[n-1] - n > 0 and a[n-1] - n is not already in the sequence. Otherwise, a[n] = a[n-1] + n.

## recaman_graphics.py
Implemented with Python's graphics package.

### Usage
Optional command line arguments: -h or --Help for Usage instructions

Usage: recaman_graphics.py --outline=\<outlinecolor\> --background=\<backgroundcolor\>

Default colors are outline = antiquewhite1 and background = lightskyblue.

Program closes when user clicks anywhere in the window.

### Method
Draw circles with radius n/2.
Circles are centered between a[n] and a[n-1].

## recaman_turtle.py
Implemented with Python's turtle package.

### Method
Draw semi-circles with radius n/2.
Semi-circles have alternating orientation and face either up or down.
Semi-cirlces begin from the endpoint of the previous semi-circle, a[n-1], and end at a[n].

## rot_triangles.py
Implemented with Python's graphics package.

### Usage
Draws random traingles. Click to create a new triangle with a random color, rotational direction and speed, and size centered around the coordinates of your mouse click. Press *q* to quit
