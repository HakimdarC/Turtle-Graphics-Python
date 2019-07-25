import turtle

t=turtle.Turtle()
b=turtle.Turtle()
t.speed(1000)
c=["green","red","blue","yellow","orange"]
def aa(c,l,w):
    t.color(c)
    t.width(w%4)
    t.left(85)
    #t.forward(5+l)
    t.right(165)
    t.forward(l)
    #t.up()
    #t.goto(26, 38)
    #t.down()
    #t.right(291)
    #t.forward(25)
t.hideturtle()
for i in range(300):
    aa(c[i%5],i,i)
    #t.up()
    #t.goto(-100, -100)
    #t.down()
    #t.right(45)
