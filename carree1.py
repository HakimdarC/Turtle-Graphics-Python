import turtle

t=turtle.Turtle()
t.speed(13)
t.begin_fill()
t.fillcolor("yellow")
r=10
t.up()
t.goto(0, 0)
t.down()
co=["green","red","blue","yellow","orange"]
for i in range(400):
    t.circle((r+i)%60,steps=6 )
    t.color(co[i%5])
    t.right(90)
t.end_fill()
t.hideturtle()
#t.goto(0, 50)
#t.goto(70, -35)
#t.goto(0, 50)
#t.goto(0, -120)

#draw_sq(200,80)

