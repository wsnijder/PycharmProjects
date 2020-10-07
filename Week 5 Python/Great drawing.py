import turtle

window = turtle.Screen()

tess = turtle.Turtle()
tess.pensize(1)
tess.color("blue")

def draw_square(animal, size):
    for _ in range(4):
        tess.forward(size)
        tess.right(90)

for index in range(90):
    draw_square(tess, index * 5)
    tess.left(6)
    tess.speed(0)

window.exitonclick()