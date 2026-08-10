# Q6 - Finite-State Morphological Parser
# No NLTK required

def parser(word):

    # Irregular plurals
    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse",
        "feet": "foot"
    }

    # State 1: Irregular plural
    if word in irregular:
        return irregular[word], "Irregular Plural"

    # State 2: Words ending with -ies
    elif word.endswith("ies"):
        return word[:-3] + "y", "Plural Noun"

    # State 3: Words ending with -es
    elif word.endswith("es"):
        return word[:-2], "Plural Noun"

    # State 4: Regular plural -s
    elif word.endswith("s"):
        return word[:-1], "Plural Noun"

    # State 5: Singular
    else:
        return word, "Singular"


# Test words
words = [
    "cars",
    "boxes",
    "cities",
    "children",
    "book"
]

print("Word\t\tRoot\t\tType")
print("------------------------------------------")

for word in words:
    root, category = parser(word)
    print(word, "\t\t", root, "\t\t", category)