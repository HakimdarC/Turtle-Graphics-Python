import turtle
t=turtle.Turtle()
co=["green","red","blue","yellow","orange"]
t.shape("turtle")
t.speed(1)
t.begin_fill()
def create_turtle():
    for i in range(233):
        t.up()
        #create_turtle()
        t.forward((i+5)%80)
        #t.color(co[i])
        #t.fillcolor(co[i])
        t.tilt(30)
        t.right(i+5)
       # t.goto(0+i, 0+i)
        #t.down()
        ##t.reset()
        #t.end_fill()

t.begin_fill()
for i in range(233):
    create_turtle()
    t.shape("turtle")
    t.color(co[i])
    t.fillcolor(co[i])
    t.reset()
    
b=turtle.Turtle()
co=["green","red","blue","yellow","orange"]
b.shape("turtle")
b.speed(1)
b.begin_fill()
def create_turtle():
    for i in range(233):
        b.up()
        #create_turtle()
        b.forward((i+5)%80)
        #t.color(co[i])
        #t.fillcolor(co[i])
        b.right(i+5)
       # t.goto(0+i, 0+i)
        #t.down()
        ##t.reset()
        #t.end_fill()

b.begin_fill()
for i in range(233):
    create_turtle()
    b.shape("turtle")
    b.color(co[i])
    b.fillcolor(co[i])
    b.reset()


    
