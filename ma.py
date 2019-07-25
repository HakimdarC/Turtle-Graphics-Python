import turtle
t = turtle.Turtle()
h = turtle.Turtle()
wn =turtle.Screen()
co=["pink","orange","red","blue","green"]

t.speed(300)
t.begin_fill()
t.color("red")
for i in range(120):
    wn.bgcolor(co[i%1])
    t.goto(0,0)
    #t.tilt(90)
    t.dot()
    t.forward(200)
    t.right(90+i%45)
    #t.circle(i%120,steps=5) #(10+i)%70)
    t.width(25)
    t.color(co[i%3])
    t.end_fill()
    t.hideturtle()


