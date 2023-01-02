import turtle as t
from random import choice


shape = t.Turtle()
shape.pensize(15)

colours = ["cyan", "yellow", "brown", "pink", "green", "black", "orange", "blue", "red"]


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360/num_sides
        shape.forward(80)
        shape.right(angle)

for current_shape in range(3,9):
    shape.color(choice(colours))
    draw_shape(current_shape)
