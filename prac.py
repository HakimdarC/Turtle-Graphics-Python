import turtle
t = turtle.Turtle()
wn =turtle.Screen()

t.shape("turtle")

co=["green","red","blue","yellow","orange"]

t.speed(13)
t.begin_fill()
for i in range(5000):
    wn.bgcolor(co[i%5])
    t.forward(1+i%70)
    t.tilt(5)
    t.right(i%360)
    t.forward(1+i%70)
    t.width((1/10+i)%60)
    t.color(co[i%5])
    t.end_fill()
