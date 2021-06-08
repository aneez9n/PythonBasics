paragraph = input("Give a paragraph :     ")
words_count = 0
for word in paragraph:
    if word == " ":
        words_count += 1
print(words_count)

