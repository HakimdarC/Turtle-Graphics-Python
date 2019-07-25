import turtle

t=turtle.Turtle()
b=turtle.Turtle()
t.speed(1000)
c=["green","red","blue","yellow","orange"]
def aa(c,l):
    t.color(c)
    t.width(2)
    t.left(35)
    t.forward(5+l)
    t.right(145)
    t.forward(130)
    #t.up()
    #t.goto(26, 38)
    #t.down()
    #t.right(291)
    #t.forward(25)
t.hideturtle()
for i in range(300):
    aa(c[i%5],i)
    #t.up()
    #t.goto(-100, -100)
    #t.down()
    #t.right(45)
