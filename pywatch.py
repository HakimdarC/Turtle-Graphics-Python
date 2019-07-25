import turtle
t = turtle.Turtle()
h = turtle.Turtle()
wn =turtle.Screen()
co=["red","orange","red","blue","green"]

t.speed(1000)
t.begin_fill()
t.color("red")
for i in range(100):
    wn.bgcolor("yellow")
    t.goto(0,0)
    #t.tilt(90)
    t.dot()
    t.right(145)
    t.forward(170)
    #t.circle(i%120,steps=5) #(10+i)%70)
    t.width(i)
    t.color(co[i%1])
    t.end_fill()
    t.hideturtle()

