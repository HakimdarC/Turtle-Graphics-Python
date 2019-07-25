from turtle import Turtle

class MyTurtle(Turtle):
    def glow(self,x,y):
        self.fillcolor("red")
    def unglow(self,x,y):
        self.fillcolor("")
        
turtle = MyTurtle()
turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
turtle.onrelease(turtle.unglow)
turtle.mainloop()
