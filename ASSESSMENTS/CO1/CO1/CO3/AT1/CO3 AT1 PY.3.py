from collections import Counter
import math

# -----------------------------
# Training Corpus
# -----------------------------

train_text = """
the student is learning python
the student is reading a book
the student is writing a program
the teacher is teaching python
the teacher is reading a book
"""

# Test Corpus
test_text = """
the student is learning python
the teacher is reading a book
"""

# Tokenization
train_words = train_text.lower().split()
test_words = test_text.lower().split()


# -----------------------------
# Create N-gram Counts
# -----------------------------

unigram = Counter(train_words)

bigram = Counter(
    (train_words[i], train_words[i + 1])
    for i in range(len(train_words) - 1)
)

trigram = Counter(
    (train_words[i], train_words[i + 1], train_words[i + 2])
    for i in range(len(train_words) - 2)
)


# -----------------------------
# Probability Functions
# -----------------------------

def unigram_probability(word):
    return unigram[word] / len(train_words)


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# -----------------------------
# Entropy Calculation
# -----------------------------

def calculate_entropy(probabilities):

    entropy = 0

    for p in probabilities:

        if p > 0:
            entropy += -p * math.log2(p)

    return entropy


# -----------------------------
# Unigram Entropy
# -----------------------------

unigram_probs = []

for word in test_words:
    p = unigram_probability(word)

    if p > 0:
        unigram_probs.append(p)

unigram_entropy = calculate_entropy(unigram_probs)


# -----------------------------
# Bigram Entropy
# -----------------------------

bigram_probs = []

for i in range(1, len(test_words)):

    p = bigram_probability(
        test_words[i - 1],
        test_words[i]
    )

    if p > 0:
        bigram_probs.append(p)

bigram_entropy = calculate_entropy(bigram_probs)


# -----------------------------
# Trigram Entropy
# -----------------------------

trigram_probs = []

for i in range(2, len(test_words)):

    p = trigram_probability(
        test_words[i - 2],
        test_words[i - 1],
        test_words[i]
    )

    if p > 0:
        trigram_probs.append(p)

trigram_entropy = calculate_entropy(trigram_probs)


# -----------------------------
# Display Results
# -----------------------------

print("N-GRAM ENTROPY RESULTS")
print("----------------------")

print("Unigram Entropy :", round(unigram_entropy, 4))
print("Bigram Entropy  :", round(bigram_entropy, 4))
print("Trigram Entropy :", round(trigram_entropy, 4))


# -----------------------------
# High and Low Entropy
# -----------------------------

print("\nInterpretation")

if unigram_entropy > bigram_entropy:
    print("Bigram model has lower uncertainty than Unigram model.")
else:
    print("Unigram model has lower uncertainty.")

print("Lower entropy means better predictability.")
print("Higher entropy means greater uncertainty.")


# -----------------------------
# Smoothing Example
# -----------------------------

print("\nSmoothing Example")

word = "football"

# Add-1 smoothing
V = len(unigram)

smoothed_probability = (
    unigram[word] + 1
) / (
    len(train_words) + V
)

print("Unseen word:", word)
print("Smoothed Probability:",
      round(smoothed_probability, 6))