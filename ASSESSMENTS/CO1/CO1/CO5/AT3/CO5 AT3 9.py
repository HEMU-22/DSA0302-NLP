from collections import Counter

text = "the boy is playing football and the boy is playing cricket"

words = text.lower().split()
bigrams = list(zip(words, words[1:]))
counts = Counter(bigrams)

previous_word = "is"

candidates = {
    word: count
    for (first, word), count in counts.items()
    if first == previous_word
}

print("Input:")
print(text)

print("\nBigram Counts:")
for word, count in candidates.items():
    print(f"P({word} | is) count =", count)

best_word = max(candidates, key=candidates.get)

print("\nMost Frequent Next Word:")
print(best_word)
