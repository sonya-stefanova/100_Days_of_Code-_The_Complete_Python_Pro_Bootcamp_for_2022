import turtle as t

dash_trace = t.Turtle()
dash_trace.pencolor("cyan")
dash_trace.pensize(13)
########### Challenge 2 - Draw a Dashed Line ########
for _ in range(40):
    dash_trace.forward(10)
    dash_trace.penup()
    dash_trace.forward(10)
    dash_trace.pendown()