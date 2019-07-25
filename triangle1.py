import turtle

t=turtle.Turtle()
t.speed(13)
t.begin_fill()
t.fillcolor("green")
r=1
t.up()
t.goto(0, 0)
t.down()
co=["green","red","blue","yellow","orange","blue","red","green","yellow","orange"]
for i in range(400):
    t.circle((r+i)%60,steps=3)
    t.color(co[i%10])
    t.right(1)
    t.tilt(30)
t.end_fill()
t.hideturtle()
#t.goto(0, 50)
#t.goto(70, -35)
#t.goto(0, 50)
#t.goto(0, -120)

#draw_sq(200,80)

