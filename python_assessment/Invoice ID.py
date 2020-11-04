


import random

output = str(random.randrange(10000, 99999))

with open("invoice.txt", "w") as myfile:
    myfile.write(output)

with open("invoice.txt", "rt") as myfile:
    last = myfile.read()

print(last)







