def mirror(input):
    mirror_string = input + input[::-1]
    return mirror_string

text = input("What is the word you want to mirror?")
print("The word mirrored is", mirror(text))