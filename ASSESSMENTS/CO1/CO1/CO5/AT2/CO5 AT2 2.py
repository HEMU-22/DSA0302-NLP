sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

relations = [
    "Cause-Effect",
    "Consequence/Sequence"
]

print("Input Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(i, ".", sentence)

print("\nDiscourse Relations:")
print("Sentence 1 -> Sentence 2:", relations[0])
print("Sentence 2 -> Sentence 3:", relations[1])

print("\nDiscourse Structure:")
print("Heavy rainfall -> Roads flooded")
print("Roads flooded -> Schools closed")
print("Schools closed -> Students attended online classes")

print("\nCoherence: HIGH")
