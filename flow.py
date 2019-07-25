import turtle

t = turtle.Turtle()
t.speed(100)
t.begin_fill()
t.fillcolor("red")
c=["green","red","blue","yellow","orange"]
t.up()
t.goto(0, 0)
t.down()
def draw_star(l,d):
    for i in range(5):
        t.forward(l)
        t.right(d)
t.end_fill()

for i in range(500):
    t.color(c[i%5])
    draw_star(309,204)
    #t.goto(i, i)
    t.down()
    
t.end_fill()
t.hideturtle()


