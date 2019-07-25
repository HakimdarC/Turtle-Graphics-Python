import turtle

t = turtle.Turtle()
t.speed(100)
t.begin_fill()
t.fillcolor("red")
#c=["green","red"]
co=["green","red","blue","yellow","orange"]
def draw_star():
    for i in range(200):
        t.forward(280-i)
        t.right(145)
        t.color(co[i%5])
        t.width(4-i%4)
t.end_fill()
t.hideturtle()
draw_star()

