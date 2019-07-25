import turtle
t = turtle.Turtle()
wn =turtle.Screen()

t.shape("turtle")

co=["green","red","blue","yellow","orange"]

t.speed(13)
t.begin_fill()
t.color("yellow")
for i in range(0,2000,9):
    wn.bgcolor(co[i%5])
    t.forward(20+i) #(10+i)%70)
    #t.tilt(35)
    t.right(200)
    t.width((1/10+i)%5)
    t.color(co[i%5])
    t.end_fill()
