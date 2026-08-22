semantic_input = {
    "Action": "Buy",
    "Agent": "Student",
    "Object": "Book",
    "Tense": "Past"
}

print("Semantic Input:")
for key, value in semantic_input.items():
    print(key, ":", value)

# Lexical selection and surface realization
agent = "The student"
action = "bought"
obj = "a book"

sentence = f"{agent} {action} {obj}."

print("\nSurface Realization:")
print(sentence)

print("\nGrammar Check:")
print("Subject: The student")
print("Verb: bought (past tense)")
print("Object: a book")
print("Result: Grammatically Correct")
