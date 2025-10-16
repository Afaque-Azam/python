# replace the word donkey with ###### in the file

word = "donkey"

with open("poem.txt") as f:
    words = f.read()

wordNew = words.replace(word, "######")

with open("poem.txt", "w") as f:
    f.write(wordNew)