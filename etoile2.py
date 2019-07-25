import turtle

t = turtle.Turtle()
t.speed(100)
t.begin_fill()
t.fillcolor("red")
#c=["green","red"]
co=["green","red","blue","yellow","orange"]
t.up()
#t.goto(0, 0)
t.down()
def draw_star(l,d):
    for i in range(5):
        t.forward(l)
        t.right(d)
t.end_fill()

for i in range(500):
    t.color(co[i%5])
    t.width(i%2)
    draw_star(50,7)
    t.goto(0, 0)
    t.down()
    
t.end_fill()
t.hideturtle()


