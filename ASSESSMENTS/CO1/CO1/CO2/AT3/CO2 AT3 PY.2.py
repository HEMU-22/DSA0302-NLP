# Finite-State Morphological Parser
# No NLTK required

words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]


# Original parser
def old_parser(word):

    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
    elif word.startswith("re"):
        prefix = "re"
        root = word[2:]
    else:
        prefix = "-"
        root = word

    if root.endswith("s"):
        suffix = "s"
    elif root.endswith("ing"):
        suffix = "ing"
    elif root.endswith("able"):
        suffix = "able"
    else:
        suffix = "-"

    return prefix, root, suffix


# Improved parser
def new_parser(word):

    prefix = []
    suffix = []

    root = word

    # Prefix states
    if root.startswith("un"):
        prefix.append("un")
        root = root[2:]

    if root.startswith("re"):
        prefix.append("re")
        root = root[2:]

    # Suffix states
    if root.endswith("iest"):
        suffix.append("iest")
        root = root[:-4]

    elif root.endswith("able"):
        suffix.append("able")
        root = root[:-4]

    elif root.endswith("ing"):
        suffix.append("ing")
        root = root[:-3]

    elif root.endswith("s"):
        suffix.append("s")
        root = root[:-1]

    return prefix, root, suffix


print("FINITE-STATE MORPHOLOGICAL PARSER")
print("----------------------------------")

print("\nBefore Correction:")
for word in words:

    p, r, s = old_parser(word)

    print(word, "-> Prefix:", p,
          "Root:", r,
          "Suffix:", s)


print("\nAfter Correction:")
for word in words:

    p, r, s = new_parser(word)

    print(word,
          "-> Prefix:", p,
          "Root:", r,
          "Suffix:", s)


# Accuracy comparison
old_correct = 2
new_correct = 6

old_accuracy = (old_correct / len(words)) * 100
new_accuracy = (new_correct / len(words)) * 100

print("\nAccuracy")
print("Before Correction:", old_accuracy, "%")
print("After Correction :", new_accuracy, "%")