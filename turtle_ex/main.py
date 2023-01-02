from turtle import Turtle, Screen

turtle_girly = Turtle()
turtle_girly.color("sea green")
turtle_girly.shape("turtle")
turtle_girly.pen(pencolor="magenta", pensize=18)

# TODO: Motion definition:
turtle_girly.speed("slowest")

turtle_girly.circle(100)
turtle_girly.forward(300)
turtle_girly.circle(80)
turtle_girly.backward(100)

screen = Screen()
screen.exitonclick()