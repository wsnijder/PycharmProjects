# two turtles created

import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

if tess is alex:
    print("there is one turtle created")
else: print("there are two turtles created")

# color applies to both turtles since it is aliased and not cloned

alex.forward(100)
