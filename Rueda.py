import turtle
turtle.bgcolor('black')
pen = turtle.Pen()
colors = ['white', 'red', 'blue', 'orange', 'green', 'yellow']

for i in range(360):
    pen.color(colors[i % 3])
    pen.forward(i)
    pen.left(120)
    pen.width(i/100 + 1)