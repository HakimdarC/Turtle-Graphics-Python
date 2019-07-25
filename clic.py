import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def right():
   tess.setheading(0)
   tess.forward(100)

turtle.onclick(right)
turtle.mainloop()


