import turtle

t = turtle.Turtle()
t.speed(1)
t.color("green")
screen = turtle.Screen()
screen.colormode(255)
screen.bgcolor("orange")
t.begin_fill()
t.fillcolor("red")
for i in range(5):
    t.circle(40)
t.end_fill()
t.hideturtle()
t.reset()
t.color("green")
t.speed(1)
t.begin_fill()
t.fillcolor("blue")
t.color("yellow")
t.circle(120,steps=6)
t.end_fill()
t.hideturtle()
t.reset()
t.speed(1)
t.begin_fill()
t.fillcolor("violet")
t.color("yellow")
for i in range(6):
    t.forward(80)
    t.right(144)
t.end_fill()
t.hideturtle()
t.reset()
t.color("green")
t.speed(1)
t.begin_fill()
t.fillcolor("blue")
t.color("yellow")
t.up()
t.goto(0, -100)
t.down()
t.circle(120)
t.end_fill()
t.hideturtle()

t.reset()
t.speed(1)
t.begin_fill()
def draw_sq(l,w):
    for i in range(4):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)


t=turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("yellow")
t.color("blue")
t.up()
t.goto(0, 100)
t.goto(0, 50)
t.goto(100, 50)
t.goto(100, 100)
t.down()
#draw_sq(200,80)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("red")
t.color("red")
t.up()
t.goto(0, 100)
t.goto(0, 50)
t.goto(-100, 50)
t.goto(-100, 100)
t.down()
#draw_sq(200,80)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("green")
t.color("green")
t.up()
t.goto(0, -100)
t.goto(0, -50)
t.goto(-100, -50)
t.goto(-100, -100)
t.down()
#draw_sq(200,80)
t.end_fill()
t.hideturtle()

t=turtle.Turtle()
t.speed(1)
t.begin_fill()
t.fillcolor("green")
t.color("yellow")
t.up()
t.goto(0, -100)
t.goto(0, -50)
t.goto(100, -50)
t.goto(100, -100)
t.down()
#draw_sq(200,80)
t.end_fill()
t.hideturtle()

