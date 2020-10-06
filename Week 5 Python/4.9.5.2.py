import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(2)
tess.color("blue")

def draw_square(animal, size):
    animal.forward(size)
    animal.right(90)

size = 2
for _ in range(90):
    tess.right(1)
    draw_square(tess, size)
    size += 4
    tess.speed(0)

window.exitonclick()