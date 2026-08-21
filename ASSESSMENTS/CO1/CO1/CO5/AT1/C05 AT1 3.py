sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

context = sentence.lower()

riverbank_clues = ["river", "flooded", "storm"]
financial_clues = ["money", "loan", "account", "deposit"]

riverbank_score = sum(word in context for word in riverbank_clues)
financial_score = sum(word in context for word in financial_clues)

if riverbank_score > financial_score:
    meaning = "riverbank"
else:
    meaning = "financial institution"

print("Input:")
print(sentence)

print("\nWSD Scores:")
print("Riverbank:", riverbank_score)
print("Financial institution:", financial_score)

print("\nResolved Meaning:", meaning)

print("\nPredicate Logic:")
print("Bank(b)")
print("River(r)")
print("Location(b,r)")
print("Storm(s)")
print("Flood(b)")
print("After(Flood(b),s)")
print("Quick(a)")
print("Action(a)")
print("Saved(b,a)")

print("\nDiscourse Relation: CONTRAST")

print("\nParaphrase:")
print("The riverbank flooded after the storm, but quick action saved it.")
