from collections import Counter

# English text corpus
text = """
The student is learning Python.
The student is reading a book.
The student is writing a program.
The teacher is teaching Python.
The teacher is reading a book.
The student is learning natural language processing.
"""

# Preprocessing
words = text.lower().replace(".", "").split()

# Create N-grams
unigrams = Counter(words)

bigrams = Counter(
    (words[i], words[i + 1])
    for i in range(len(words) - 1)
)

trigrams = Counter(
    (words[i], words[i + 1], words[i + 2])
    for i in range(len(words) - 2)
)

# Display counts and probabilities
print("UNIGRAM COUNTS")
for word, count in unigrams.items():
    probability = count / len(words)
    print(word, ":", count, "Probability:", round(probability, 3))

print("\nBIGRAM COUNTS")
for pair, count in bigrams.items():
    probability = count / unigrams[pair[0]]
    print(pair, ":", count, "Probability:", round(probability, 3))

print("\nTRIGRAM COUNTS")
for tri, count in trigrams.items():
    probability = count / bigrams[tri[:2]]
    print(tri, ":", count, "Probability:", round(probability, 3))


# Select N
n = int(input("\nEnter N (1, 2, or 3): "))

if n == 1:
    print("\nUnigram Model Selected")

elif n == 2:
    print("\nBigram Model Selected")

elif n == 3:
    print("\nTrigram Model Selected")

else:
    print("Invalid N")


# Top-5 next word prediction
sentence = input("\nEnter incomplete sentence: ").lower().split()

print("\nTop-5 Next Word Predictions:")

if n == 1:
    results = unigrams.most_common(5)

elif n == 2:
    last_word = sentence[-1]

    candidates = []

    for pair, count in bigrams.items():
        if pair[0] == last_word:
            probability = count / unigrams[last_word]
            candidates.append((pair[1], probability))

    results = sorted(candidates, key=lambda x: x[1], reverse=True)[:5]

elif n == 3:
    if len(sentence) >= 2:
        last_two = tuple(sentence[-2:])
        candidates = []

        for tri, count in trigrams.items():
            if tri[:2] == last_two:
                probability = count / bigrams[last_two]
                candidates.append((tri[2], probability))

        results = sorted(
            candidates,
            key=lambda x: x[1],
            reverse=True
        )[:5]
    else:
        results = []

if n == 1:
    for word, count in results:
        print(word, "Probability:", round(count / len(words), 3))
else:
    for word, probability in results:
        print(word, "Probability:", round(probability, 3))


# Unseen N-gram demonstration
print("\nUnseen N-gram Example")

test_bigram = ("student", "football")

if test_bigram in bigrams:
    probability = bigrams[test_bigram] / unigrams[test_bigram[0]]
else:
    probability = 0

print(test_bigram, "Probability:", probability)