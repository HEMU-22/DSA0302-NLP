# POS Tagging using Rule-Based,
# Stochastic and Transformation-Based methods

# Penn Treebank Tagset

words = input("Enter a sentence: ").lower().split()


# --------------------------------
# 1. RULE-BASED POS TAGGER
# --------------------------------

dictionary = {
    "i": "PRP",
    "you": "PRP",
    "he": "PRP",
    "she": "PRP",
    "we": "PRP",
    "they": "PRP",

    "the": "DT",
    "a": "DT",
    "an": "DT",

    "is": "VBZ",
    "am": "VBP",
    "are": "VBP",
    "was": "VBD",
    "were": "VBD",

    "and": "CC",
    "but": "CC",
    "or": "CC",

    "in": "IN",
    "on": "IN",
    "at": "IN",
    "from": "IN",

    "good": "JJ",
    "beautiful": "JJ",
    "happy": "JJ",

    "quickly": "RB",
    "slowly": "RB",

    "play": "VB",
    "read": "VB",
    "write": "VB",
    "learn": "VB"
}


def rule_based(words):

    tags = []

    for word in words:

        if word in dictionary:
            tags.append(dictionary[word])

        elif word.endswith("ly"):
            tags.append("RB")

        elif word.endswith("ing"):
            tags.append("VBG")

        elif word.endswith("ed"):
            tags.append("VBD")

        elif word.endswith("s"):
            tags.append("NNS")

        else:
            tags.append("NN")

    return tags


# --------------------------------
# 2. STOCHASTIC POS TAGGER
# --------------------------------

# Simple word/tag probability knowledge

stochastic_tags = {
    "i": "PRP",
    "you": "PRP",
    "the": "DT",
    "a": "DT",
    "student": "NN",
    "teacher": "NN",
    "play": "VB",
    "plays": "VBZ",
    "playing": "VBG",
    "good": "JJ",
    "quickly": "RB",
    "is": "VBZ",
    "am": "VBP",
    "are": "VBP",
    "and": "CC",
    "in": "IN"
}


def stochastic(words):

    tags = []

    for word in words:

        if word in stochastic_tags:
            tags.append(stochastic_tags[word])
        else:
            tags.append("NN")

    return tags


# --------------------------------
# 3. TRANSFORMATION-BASED TAGGER
# --------------------------------

def transformation(words, tags):

    new_tags = tags.copy()

    for i in range(len(words)):

        # Rule:
        # Word after pronoun or auxiliary verb
        # can be a verb.

        if i > 0:

            previous = words[i - 1]

            if previous in ["i", "you", "we", "they"]:
                if words[i].endswith("ing"):
                    new_tags[i] = "VBG"
                elif words[i] in ["play", "read", "write", "learn"]:
                    new_tags[i] = "VB"

            if previous in ["is", "am", "are", "was", "were"]:
                if words[i].endswith("ing"):
                    new_tags[i] = "VBG"

    return new_tags


# --------------------------------
# Execute
# --------------------------------

rule_tags = rule_based(words)

stochastic_tags_result = stochastic(words)

transformed_tags = transformation(
    words,
    stochastic_tags_result
)


# --------------------------------
# Display
# --------------------------------

print("\nPOS TAGGING RESULTS")
print("-------------------")

print("\nRule-Based Tagging:")
for word, tag in zip(words, rule_tags):
    print(word, "->", tag)


print("\nStochastic Tagging:")
for word, tag in zip(words, stochastic_tags_result):
    print(word, "->", tag)


print("\nTransformation-Based Tagging:")
for word, tag in zip(words, transformed_tags):
    print(word, "->", tag)


print("\nPenn Treebank Tags:")
print("NN  = Noun")
print("VB  = Verb")
print("JJ  = Adjective")
print("RB  = Adverb")
print("PRP = Pronoun")
print("IN  = Preposition")
print("CC  = Conjunction")