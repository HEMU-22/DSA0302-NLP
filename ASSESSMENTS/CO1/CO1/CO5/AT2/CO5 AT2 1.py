text = "Ravi met Arun at the library. He borrowed a book and later returned it."

entities = ["Ravi", "Arun"]
resolution = {
    "He": "Ravi",
    "it": "book"
}

print("Input:")
print(text)

print("\nEntity Resolution:")
for pronoun, entity in resolution.items():
    print(pronoun, "->", entity)

resolved = "Ravi met Arun at the library. Ravi borrowed a book and later returned the book."

print("\nResolved Discourse:")
print(resolved)

print("\nEntity Chains:")
print("Ravi -> He")
print("book -> it")
