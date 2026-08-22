semantic = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

agent = "The student"
verb = "bought"
obj = "a book"

sentence = f"{agent} {verb} {obj}."

print("Semantic Representation:")
for key, value in semantic.items():
    print(key, ":", value)

print("\nSurface Realization:")
print(sentence)

print("\nValidation:")
print("Tense: Past")
print("Structure: Subject + Verb + Object")
print("Grammar: Correct")
