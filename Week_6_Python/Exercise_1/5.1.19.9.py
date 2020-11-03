def remove_letter(letter, word):
    without_letter = ""
    for c in word:
        if c not in word:
            without_letter += c
    return without_letter

remove_letter("a", "apple")
