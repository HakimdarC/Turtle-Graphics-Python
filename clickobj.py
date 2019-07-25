import turtle
turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("purple")
tess.begin_fill()
tess.circle(44)
tess.fillcolor("orange")
tess.end_fill()

tess.begin_fill()
def chng():
    tess.color("pink")
    tess.circle(44)
    tess.fillcolor("orange")
    tess.end_fill()
      
tess.onscreenclick(chng)
tess.listen()


def turn(x, y):
    t.left(180)
    onclick(turn)  # Now clicking into the turtle will turn it.
    onclick(None)  # event-binding will be removed
class MyTurtle(turtle.Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")

tess.onscreenclick(tess.glow)     # clicking on turtle turns fillcolor red,
tess.onrelease(tess.unglow) # releasing turns it to transparent.
