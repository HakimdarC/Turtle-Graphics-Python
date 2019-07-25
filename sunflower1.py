import turtle

t = turtle.Turtle()
t.speed(100)
t.begin_fill()
t.fillcolor("red")
c=["green","red","blue","yellow","orange"]
t.up()
t.goto(-200, -200)
t.down()
def draw_star(l,d):
    for i in range(5):
        t.forward(l)
        t.right(d)
t.end_fill()

for i in range(500):
    t.color(c[i%5])
    t.width
    draw_star(302,24)
    #t.goto(i, i)
    t.down()
    
t.end_fill()
t.hideturtle()


