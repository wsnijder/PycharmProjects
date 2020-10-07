import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t = turtle.Turtle()
t.color("pink")
t.pensize(3)

def draw_triangle(t, sz):
    for _ in range(5):
        t.forward(sz)
        t.right(144)

for _ in range(5):
    draw_triangle(t, 100)
    t.penup()
    t.forward(350)
    t.right(144)
    t.pendown()
    t.speed(0)



window.exitonclick()