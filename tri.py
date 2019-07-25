import turtle

t=turtle.Turtle()
t.speed(100)
t.begin_fill()
t.fillcolor("yellow")

t.up()
t.goto(0, 0)
t.down()
for i in range(50):
    t.circle(10+i,extent=45,steps=3)
    t.color("green")
    t.right(20)
t.end_fill()
t.hideturtle()
#t.goto(0, 50)
#t.goto(70, -35)
#t.goto(0, 50)
#t.goto(0, -120)

#draw_sq(200,80)

