import turtle
t = turtle.Turtle()
wn =turtle.Screen()

t.shape("turtle")

co=["green","red","blue","yellow","orange"]

t.speed(100)
t.begin_fill()
t.color("yellow")
l=[]
for i in range(700):
    wn.bgcolor(co[i%5])
    l.append(i)
    #t.tilt(90)
    t.dot()
    t.forward(int(l[::-1]))
    t.right(19)
    #t.circle(i%120,steps=5) #(10+i)%70)
    t.width((1/10+i)%1)
    t.color(co[i%5])
    t.end_fill()
