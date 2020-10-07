import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.pensize(3)

def draw_triangle(t, sz):
    for _ in range(5):
        t.forward(sz)
        t.right(144)

draw_triangle(t,100)

window.exitonclick()
