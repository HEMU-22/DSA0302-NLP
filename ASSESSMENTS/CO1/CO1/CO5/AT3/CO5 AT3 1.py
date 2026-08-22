text = "Ravi went to the library. He borrowed a book and later returned it."

resolution = {
    "He": "Ravi",
    "it": "book"
}

print("Input:")
print(text)

print("\nReference Resolution:")
for pronoun, entity in resolution.items():
    print(pronoun, "->", entity)

print("\nResolved Text:")
print("Ravi went to the library. Ravi borrowed a book and later returned the book.")
