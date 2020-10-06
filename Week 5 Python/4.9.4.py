import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("blue")

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

size = 80
for _ in range(20):
    tess.right(18)
    draw_square(tess,size)
    tess.speed(0)

window.exitonclick()