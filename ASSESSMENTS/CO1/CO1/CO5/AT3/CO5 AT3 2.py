sentences = [
    "The roads were flooded after heavy rainfall.",
    "Therefore, schools were closed for the day.",
    "Students attended classes online."
]

print("Input:")
for i, sentence in enumerate(sentences, 1):
    print(i, ".", sentence)

print("\nDiscourse Relations:")
print("Sentence 1 -> Sentence 2 : Cause-Effect")
print("Sentence 2 -> Sentence 3 : Consequence/Sequence")

print("\nCoherence Chain:")
print("Heavy rainfall -> Roads flooded -> Schools closed -> Online classes")

print("\nCoherence: HIGH")
