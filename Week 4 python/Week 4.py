import turtle

def draw_square(animal, size):
    """
    Draw a square
    """
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

# non-fruitful function
def calculate_surface_of_square(side_length):
    surface = side_length ** 2
    print(surface)
    return surface

screen = turtle.Screen()
nick = turtle.Turtle()

for index in range(6):
    draw_square(nick, index * 5)
    nick.left(6)

    result = calculate_surface_of_square()

screen.exitonclick()
