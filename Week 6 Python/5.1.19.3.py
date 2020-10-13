def count_letters(word):
    result = len(word)
    return result


answer = str(input("name a word"))
calculation = count_letters(answer)
print("number of letters is", calculation)