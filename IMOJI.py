import turtle
t = turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("pink")
t.speed(1)
t.begin_fill()
t.width(5)
t.circle(80)
t.fillcolor("yellow")
t.color("yellow")
def imo():

t.begin_fill()
t.fillcolor("black")
t.color("white")
t.up()
t.goto(40, 85)
t.down()
t.circle(10)
t.end_fill()


t.begin_fill()
t.fillcolor("black")
t.color("white")
t.up()
t.goto(-40, 85)
t.down()
t.circle(10)
t.end_fill()

t.begin_fill()
t.fillcolor("black")
t.up()
t.goto(-40, 80)
t.down()
t.circle(20)
t.end_fill()

t.begin_fill()
t.fillcolor("black")
t.up()
t.goto(-40, 80)
t.down()
t.circle(20)
t.end_fill()

t.up()
t.goto(-32, 40)
t.down()
t.color("red")
t.width(3)
t.right(9)
t.forward(20)
t.left(9)
t.forward(20)
t.left(9)
t.forward(20)
t.hideturtle()


for i in range(200):
    imo()
    t.up()
    t.goto(-40+100+i, 80+200+i)
    t.down()
    

