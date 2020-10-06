import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.color('pink')
        animal.forward(size)
        animal.left(90)
    animal.forward(size * 2)

window = turtle.Screen()
window.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.pensize(3)

for _ in range(5):
    draw_square(ferdi, 20)
    tess.speed(0)

window.exitonclick()