# Q7 - Morphological Feature Extraction
# No NLTK required

documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]


# Simple stemming function
def stem(word):

    if word.endswith("ing"):
        return word[:-3]

    elif word.endswith("ed"):
        return word[:-2]

    elif word.endswith("s"):
        return word[:-1]

    else:
        return word


# -------------------------------
# Original Vocabulary
# -------------------------------

original_words = []

for document in documents:
    words = document.lower().split()
    original_words.extend(words)

original_vocabulary = set(original_words)


# -------------------------------
# Stemming BEFORE Feature Extraction
# -------------------------------

processed_words = []

for document in documents:

    words = document.lower().split()

    for word in words:
        processed_words.append(stem(word))


processed_vocabulary = set(processed_words)


# -------------------------------
# Display Results
# -------------------------------

print("ORIGINAL VOCABULARY")
print("-------------------")

for word in sorted(original_vocabulary):
    print(word)

print("\nOriginal Vocabulary Size:")
print(len(original_vocabulary))


print("\nAFTER STEMMING")
print("--------------")

for word in sorted(processed_vocabulary):
    print(word)

print("\nNew Vocabulary Size:")
print(len(processed_vocabulary))


print("\nVocabulary Reduction:")
print(
    len(original_vocabulary)
    - len(processed_vocabulary)
)