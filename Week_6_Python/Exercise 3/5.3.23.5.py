def add_vectors(vector1, vector2):
    if len(vector1) != len(vector2):
        return None
    vector3 = []

    for v1, v2 in zip(vector1, vector2):
        vector3.append(v1 + v2)

    sumvector = 0
    for vector_3 in vector3:
        sumvector += vector_3
print(add_vectors([1,1], [1,1]))
#Does not work!!