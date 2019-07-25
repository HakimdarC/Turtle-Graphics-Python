import turtle

t=turtle.Turtle()
t.speed(13)
t.begin_fill()
t.fillcolor("yellow")
r=70
t.up()
t.goto(0, 0)
t.down()
co=["green","red","blue","yellow","orange"]
for i in range(400):
    t.circle(r,steps=4 )
    t.color(co[i%5])
    t.right(55)
    t.width(i%4)
t.end_fill()
t.hideturtle()
#t.goto(0, 50)
#t.goto(70, -35)
#t.goto(0, 50)
#t.goto(0, -120)

#draw_sq(200,80)

