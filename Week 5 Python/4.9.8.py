import math

def area_of_circle(r):
    result = (r**2 * math.pi)
    return result

answer = int(input("What is the radius of your circle?"))
calculation = area_of_circle(answer)
print("The area is", calculation)
