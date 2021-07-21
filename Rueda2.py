import turtle
turtle.bgcolor('black')
pen = turtle.Pen()
colors = ['']

for i in range(4):
    pen.color(colors[i % 4])
    pen.forward(i)
    pen.right(20)
    pen.width(i/100 + 3)