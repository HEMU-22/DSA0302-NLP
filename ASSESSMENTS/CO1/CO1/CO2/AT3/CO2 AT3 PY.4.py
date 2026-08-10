# Morphological Error Analysis
# E-commerce Product Search
# No NLTK required

words = [
    "watches",
    "watching",
    "washable",
    "washer",
    "washed"
]


# Simple Porter-style suffix removal
def stem_word(word):

    if word.endswith("able"):
        return word[:-4]

    elif word.endswith("ing"):
        return word[:-3]

    elif word.endswith("ed"):
        return word[:-2]

    elif word.endswith("es"):
        return word[:-2]

    elif word.endswith("s"):
        return word[:-1]

    elif word.endswith("er"):
        return word[:-2]

    else:
        return word


print("E-COMMERCE MORPHOLOGICAL ERROR ANALYSIS")
print("----------------------------------------")

print("Word\t\tStem\t\tType")

for word in words:

    stem = stem_word(word)

    # Classification
    if word in ["watches", "watching", "washed"]:
        typ = "Inflectional"

    else:
        typ = "Derivational"

    print(word, "\t\t", stem, "\t\t", typ)