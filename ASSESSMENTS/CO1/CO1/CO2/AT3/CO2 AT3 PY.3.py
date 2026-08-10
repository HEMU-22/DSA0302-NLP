# News Classification - Stemming Error Analysis
# No NLTK required

words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization's"
]


# -------------------------------
# 1. Without Stemming
# -------------------------------

print("WITHOUT STEMMING")
print("----------------")

for word in words:
    print(word)


# -------------------------------
# 2. Simple Porter-style Stemming
# -------------------------------

def stem_word(word):

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


print("\nPORTER-STYLE STEMMING")
print("---------------------")

for word in words:
    print(word, "->", stem_word(word))


# -------------------------------
# 3. Simple Lemmatization
# -------------------------------

def lemmatize_word(word):

    word = word.replace("'s", "")

    if word == "organization":
        return "organization"

    elif word == "organizer":
        return "organizer"

    elif word == "organizing":
        return "organize"

    elif word == "organized":
        return "organize"

    else:
        return word


print("\nLEMMATIZATION")
print("-------------")

for word in words:
    print(word, "->", lemmatize_word(word))


# -------------------------------
# Comparison
# -------------------------------

print("\nCOMPARISON")
print("----------")

print("Without Stemming : Preserves original words")
print("Stemming         : Removes suffixes")
print("Lemmatization    : Produces meaningful base forms")

print("\nBest Strategy: Lemmatization")