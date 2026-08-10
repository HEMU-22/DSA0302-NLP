from collections import Counter

# English corpus
text = """
the student is learning python
the student is reading a book
the student is writing a program
the teacher is teaching python
the teacher is reading a book
the student is learning nlp
the student is studying language
"""

# Preprocessing
words = text.lower().split()

# N-gram counts
unigram = Counter(words)

bigram = Counter(
    (words[i], words[i + 1])
    for i in range(len(words) - 1)
)

trigram = Counter(
    (words[i], words[i + 1], words[i + 2])
    for i in range(len(words) - 2)
)

total_words = len(words)


# Unigram probability
def unigram_probability(word):
    return unigram[word] / total_words


# Bigram probability
def bigram_probability(previous, word):
    if unigram[previous] == 0:
        return 0

    return bigram[(previous, word)] / unigram[previous]


# Trigram probability
def trigram_probability(w1, w2, word):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, word)] / bigram[(w1, w2)]


# Get possible next words
vocabulary = list(unigram.keys())


# 1. Unsmoothed model
def unsmoothed_prediction(sentence):
    previous = sentence[-1]

    candidates = []

    for word in vocabulary:
        p = bigram_probability(previous, word)

        if p > 0:
            candidates.append((word, p))

    if candidates:
        return max(candidates, key=lambda x: x[1])

    return ("No prediction", 0)


# 2. Backoff model
def backoff_prediction(sentence):

    if len(sentence) >= 2:
        w1 = sentence[-2]
        w2 = sentence[-1]

        candidates = []

        for word in vocabulary:

            # Try trigram
            p = trigram_probability(w1, w2, word)

            # Backoff to bigram
            if p == 0:
                p = bigram_probability(w2, word)

            # Backoff to unigram
            if p == 0:
                p = unigram_probability(word)

            candidates.append((word, p))

        return max(candidates, key=lambda x: x[1])

    return unsmoothed_prediction(sentence)


# 3. Deleted Interpolation
def interpolation_prediction(sentence):

    if len(sentence) < 2:
        return unsmoothed_prediction(sentence)

    w1 = sentence[-2]
    w2 = sentence[-1]

    candidates = []

    # Interpolation weights
    lambda1 = 0.2
    lambda2 = 0.3
    lambda3 = 0.5

    for word in vocabulary:

        p1 = unigram_probability(word)
        p2 = bigram_probability(w2, word)
        p3 = trigram_probability(w1, w2, word)

        probability = (
            lambda1 * p1 +
            lambda2 * p2 +
            lambda3 * p3
        )

        candidates.append((word, probability))

    return max(candidates, key=lambda x: x[1])


# User input
sentence = input("Enter a sentence: ").lower().split()

print("\nPrediction Results")
print("------------------")

# Unsmoothed
word, probability = unsmoothed_prediction(sentence)
print("Unsmoothed Model :", word,
      "Probability:", round(probability, 4))

# Backoff
word, probability = backoff_prediction(sentence)
print("Backoff Model    :", word,
      "Probability:", round(probability, 4))

# Deleted Interpolation
word, probability = interpolation_prediction(sentence)
print("Interpolation    :", word,
      "Probability:", round(probability, 4))