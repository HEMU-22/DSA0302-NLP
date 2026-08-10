# Biomedical Morphological Error Analysis
# No NLTK required

words = [
    "infection",
    "infectious",
    "infected",
    "infect",
    "infections",
    "infecting"
]

def simple_stem(word):

    if word.endswith("ions"):
        return word[:-4]

    elif word.endswith("ion"):
        return word[:-3]

    elif word.endswith("ious"):
        return word[:-4]

    elif word.endswith("ed"):
        return word[:-2]

    elif word.endswith("ing"):
        return word[:-3]

    elif word.endswith("s"):
        return word[:-1]

    else:
        return word


print("Biomedical Morphological Error Analysis")
print("----------------------------------------")
print("Word\t\tStem")
print("----------------------------------------")

for word in words:
    stem = simple_stem(word)
    print(word, "\t\t", stem)