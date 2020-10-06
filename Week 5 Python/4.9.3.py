import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)
t.color("pink")

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(45)

draw_poly(t, 8, 50)


window.exitonclick()
