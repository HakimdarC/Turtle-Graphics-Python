import turtle
t=turtle.Turtle()

c=['red','green','blue','yellow','violet']
t.speed(100)
t.color("orange")
circle_size = 100
t.begin_fill()
for i in range(80):
    t.color(c[i%5])
    t.fillcolor(c[i%5])          
    t.circle(circle_size)
    t.right(10)
t.end_fill()
