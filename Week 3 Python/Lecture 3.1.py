import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.forward(50)

leonardo.stamp()
leonardo.penup()
leonardo.forward(50)
leonardo.pendown()
leonardo.stamp()

leonardo.forward(50)
leonardo.left(50)
leonardo.stamp()
leonardo.right(50)

#when this code is not used, the drawing will immediately disappear
paper.exitonclick()
