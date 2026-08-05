words = input("Enter 3 words separated by space: ").split()

print("Word\t\tRoot\t\tSuffix\t\tGrammar\t\t\tNormalized")

for word in words:

    if word == "create":
        root = "create"
        suffix = "-"
        grammar = "Base Form"

    elif word == "creates":
        root = "create"
        suffix = "s"
        grammar = "Third Person"

    elif word == "creating":
        root = "create"
        suffix = "ing"
        grammar = "Present Participle"

    else:
        root = word
        suffix = "-"
        grammar = "Unknown"

    print(f"{word}\t{root}\t\t{suffix}\t\t{grammar}\t\t{root}")