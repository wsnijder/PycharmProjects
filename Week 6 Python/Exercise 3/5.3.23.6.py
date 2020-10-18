def scalar_mult(scalar, vector):
    outcomevector = []
    for element in vector:
        outcomevector.append(scalar * vector)
    return outcomevector

print(scalar_mult(3, [1,2]))

