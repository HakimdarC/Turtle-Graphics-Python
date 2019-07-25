import turtle
from math import sin
t=turtle.Turtle()
t.speed(100)
c=["green","red","blue","violet","yellow","orange"]
circle_size = math.sin(26)
t.begin_fill()

for i in range(40):
    t.color(c[i%6])
    t.width(10)
    
    t.fillcolor("pink")          
    t.circle(circle_size)
    t.right(10)
t.end_fill()
