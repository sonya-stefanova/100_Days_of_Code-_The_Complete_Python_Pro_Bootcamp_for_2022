from turtle import Turtle, Screen
import heroes

square_shape = Turtle()

square_shape.pencolor("blue")
square_shape.fillcolor("red")
square_shape.pensize(30)

for _ in range(4):
    square_shape.forward(100)
    square_shape.left(90)

hero = heroes.gen()
print(hero)
screen = Screen()
screen.exitonclick()