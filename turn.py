import turtle

t=turtle.Turtle()
b=turtle.Turtle()
t.speed(1000)
c=["green","red","blue","yellow","orange"]
def aa(c,l,w):
    t.color(c)
    t.width(w)
    t.left(45)
    t.forward(30+l)
    #t.right(125)
    #t.forward(140)
    #t.up()
    #t.goto(26, 38)
    #t.down()
    #t.right(291)
    #t.forward(85)
t.hideturtle()
for i in range(300):
    aa(c[i%5],i,i%9)
    #t.up()
    #t.goto(-100, -100)
    #t.down()
    #t.right(45)
