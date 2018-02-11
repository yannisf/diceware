from random import randint

wordlist = {}
with open("wordlist.txt") as f:
    for line in f:
        (key, value) = line.split()
        wordlist[key] = value

words = list()
for trial in range(6):
    word_index = str()
    for roll in range(5):
        word_index += str(randint(1, 6))
    words.append(wordlist[word_index])

print(" ".join(words))
