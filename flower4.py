import turtle
t=turtle.Turtle()
t.speed(100)
c=["green","red","blue","violet","yellow","orange"]
#circle_size = 2
r=1
t.begin_fill()
for i in range(1000):
    t.color(c[i%6])
    circle_size = r/10+i
    #t.width(10)
    t.fillcolor("pink")          
    t.circle(circle_size)
    t.right(40)
t.end_fill()
