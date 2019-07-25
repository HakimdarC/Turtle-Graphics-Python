import turtle
t = turtle.Turtle()
wn =turtle.Screen()

t.shape("turtle")

co=["green","red","blue","yellow","orange"]

t.speed(100)
t.begin_fill()
t.color("yellow")
for i in range(880):
    wn.bgcolor(co[i%5])
    t.circle(i%120,steps=4) #(10+i)%70)
    #t.tilt(90)
    t.right(90)
    t.width((1/10+i)%5)
    t.color(co[i%5])
    t.end_fill()
