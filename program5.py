words = input("Enter words: ").split()

print("Word Stemming")
print("-------------")

for word in words:
    if word.endswith("ing"):
        stem = word[:-3]
    elif word.endswith("ed"):
        stem = word[:-2]
    elif word.endswith("ies"):
        stem = word[:-3] + "y"
    elif word.endswith("s"):
        stem = word[:-1]
    else:
        stem = word

    print(word, "->", stem)