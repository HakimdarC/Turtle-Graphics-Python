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
    t.circle((r+i)%90,extent=45,steps=23 )
    t.color(co[i%5])
    t.right(120)
t.end_fill()
t.hideturtle()
#t.goto(0, 50)
#t.goto(70, -35)
#t.goto(0, 50)
#t.goto(0, -120)

#draw_sq(200,80)

