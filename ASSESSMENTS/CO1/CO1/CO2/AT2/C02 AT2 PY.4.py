words = input("Enter 3 words separated by space: ").split()

print("Word\t\tPrefix\tRoot\t\tSuffix\t\tType\t\tNormalized")

for word in words:

    if word == "activate":
        prefix = "-"
        root = "activate"
        suffix = "-"
        typ = "Base"

    elif word == "activation":
        prefix = "-"
        root = "activate"
        suffix = "ion"
        typ = "Derivational"

    elif word == "reactivation":
        prefix = "re"
        root = "activate"
        suffix = "ion"
        typ = "Derivational"

    else:
        prefix = "-"
        root = word
        suffix = "-"
        typ = "Unknown"

    print(f"{word}\t{prefix}\t{root}\t{suffix}\t{typ}\t\t{root}")