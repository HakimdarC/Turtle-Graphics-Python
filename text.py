import turtle

t=turtle.Screen()
tt1=turtle.Turtle()

turtle.write("hello", move=True, align="left", font=("Arial", 23, "bold"))
        
def drawGridMark (ttl, x, y, isVertical):
  if isVertical :
    drawLine (ttl, x, y + 5, x, y - 5)
  else:
    drawLine (ttl, x - 5, y, x + 5, y)


drawGridMark(tt1, 0, 99, isVertical)
