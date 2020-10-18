poem = """Reinder Evert is a very good looking guy who is really attractive and also very smart. He is rarely seen 
outside the house and therefore he has a lack of vitamin D"""

lossewoorden = poem.split(" ")

def count_words(text):
    return len(lossewoorden)

def count_words_containing(text, letter):
    count = 0
    for word in lossewoorden:
        if letter in word:
            count += 1
    return count

letter = "e"
count = count_words(poem)
ecount = count_words_containing(poem, letter)
epercentage = (ecount/count) *100

print("Your text containt {} words, of which {} contain an e, which is about {} %".format(count, ecount, epercentage))







