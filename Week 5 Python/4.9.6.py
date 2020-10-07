import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)
t.color("blue")

def draw_equitriangle(t, n, sz):
    for _ in range(n):
        sz += 4
        t.speed(0)
draw_equitriangle(t, 80, 3)

window.exitonclick()