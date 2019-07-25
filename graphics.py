import turtle

t=turtle.Turtle()
colors = ['red', 'purple', 'blue', 'green', 'orange']
for x in range(150):
    t.color(colors[x % 5])
    t.width(x/10 + 1)
    t.forward(x)
    t.right(59)
