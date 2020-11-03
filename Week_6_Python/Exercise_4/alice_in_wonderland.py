#retrieve the book

url = "https://www.gutenberg.org/files/11/11-0.txt"
file_name = "alice.txt"
urllib.request.urlretrieve(url, file_name)


#read the book

with open(file_name) as alice_book:
    alice_text = alice_book.read()

#process the book
words = alice_text.lower().split()
word_count = {}

for word in words:
    word = word.strip("!\"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~")
    #Note that I removed the - sign since it is a single word in this case
    if len(word) > 0 and word[0].isalpha():         #isalpha means whether it is in the alphabet
        word_count(word) = word_count.get(word, 0) + 1

#get the longest word
longest_word = ""
for word in word_count:
    if len(word) > len(longest_word):
        longest_word = word

#print to output file
with open("alice_words.txt", "w") as alice_output:
    string_format = "{:<" +str(len(longest_word)) + "} {:<5}\n"

    alice_output.write(string_format.format("Word", "Count"))
    alice_output.write("=" * (len(longest_word) + 6) + "\n")

    for word in sorted(word_count):
        alice_output.write(string_format.format(word, word_count[word]))








