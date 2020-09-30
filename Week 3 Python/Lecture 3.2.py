import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

colors = ['red', 'green', 'yellow', 'blue', 'orange']
for element in range(12):
    leonardo.color(colors[element % len(colors)])
    if element % 2 == 0:
        leonardo.forward(80)
    else:
        leonardo.forward(80)
        leonardo.left(30)

    leonardo.left(30)

paper.exitonclick()