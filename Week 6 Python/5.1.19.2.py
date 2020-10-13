prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter in (prefixes[5], prefixes[7]):
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)