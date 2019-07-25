import turtle

t = turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("red")
t.color("yellow")
t.up()
t.goto(0, 0)
t.down()
def draw_star(l,d):
    for i in range(6):
        t.forward(l)
        t.right(d)

draw_star(50,144)
t.end_fill()
t.hideturtle()


