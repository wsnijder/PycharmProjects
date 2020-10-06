import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)
tess.color("pink")

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)
    animal.penup()
    animal.right(90)
    animal.forward(10)
    animal.right(90)
    animal.forward(10)
    animal.right(180)
    animal.pendown()

size = 20
for _ in range(5):
    draw_square(tess, size)
    size += 20

window.exitonclick()

