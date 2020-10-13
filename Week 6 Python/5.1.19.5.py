poem = """Reinder Evert is a very good looking guy who is really attractive and also very smart. He is rarely seen 
outside the house and therefore he has a lack of vitamin D"""

lossewoorden = poem.split(" ")
wordcount = len(lossewoorden)
ecount = 0
epercentage = ecount/wordcount *100

for letter in poem:
    if "e" in lossewoorden:
        ecount = ecount + 1

print("Your text contains", wordcount, "words, of which", ecount, "(" + epercentage + "%) words contain an e")






