sentence = input("Enter a sentence: ")

total = 0
for letter in sentence:
    if (letter == " ") or (letter == "."):
        pass
    else:
        total += 1

print("Number of words in sentence: ", total)

print(sentence[::-1])
