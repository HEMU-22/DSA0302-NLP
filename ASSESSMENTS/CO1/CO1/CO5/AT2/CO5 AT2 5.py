source = "The boy is playing football."

# Step 1: Source analysis
interlingua = {
    "Action": "PLAY",
    "Agent": "BOY",
    "Object": "FOOTBALL",
    "Tense": "PRESENT_CONTINUOUS"
}

# Step 2: Candidate translations
candidates = {
    "சிறுவன் கால்பந்து விளையாடுகிறான்.": 0.97,
    "சிறுவன் கால்பந்து விளையாடினான்.": 0.75
}

best_translation = max(candidates, key=candidates.get)

print("Source:")
print(source)

print("\nInterlingua:")
for key, value in interlingua.items():
    print(key, "=", value)

print("\nCandidate Translations and Scores:")
for translation, score in candidates.items():
    print(translation, "->", score)

print("\nFinal Translation:")
print(best_translation)

print("\nEvaluation:")
print("Interlingua preserves meaning and tense.")
print("Statistical scoring selects the highest-scoring candidate.")
