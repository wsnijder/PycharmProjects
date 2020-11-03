def reverse(input):
    rev_string = input[::-1]
    return rev_string

text = input("What is the word you want to reverse?")
print("The word backwards is", reverse(text))
