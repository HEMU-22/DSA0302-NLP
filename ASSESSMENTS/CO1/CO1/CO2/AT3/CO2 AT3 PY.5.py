# Q5 - Stemming Error Analysis
# No NLTK required

words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization's"
]


def simple_stem(word):

    word = word.replace("'s", "")

    if word.endswith("ization"):
        return word[:-7]

    elif word.endswith("izer"):
        return word[:-4]

    elif word.endswith("ing"):
        return word[:-3]

    elif word.endswith("ed"):
        return word[:-2]

    else:
        return word


print("Original Word\tStem")
print("-------------------------")

for word in words:
    stem = simple_stem(word)
    print(word, "\t\t", stem)