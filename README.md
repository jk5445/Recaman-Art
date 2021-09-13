# Recaman Drawing
In this project I will introduce myself to some Python graphics tools using the recaman sequence. Hello world of mathematical art!

## Recaman Sequence
The recaman sequence is a defined by a recurrence relation that begins at 0. a[n] = a[n-1] - n if a[n-1] - n > 0 and a[n-1] - n is not already in the sequence. Otherwise, a[n] = a[n-1] + n.

## Rules
Draw semi-circles with diameter n.
Semi-circles have alternating orientation and face either up or down.
Semi-cirlces begin from the endpoint of the previous semi-circle, a[n-1], and end at a[n]

## Implementation
I use Pythons pre-installed turtle to draw Recaman semi-circles
