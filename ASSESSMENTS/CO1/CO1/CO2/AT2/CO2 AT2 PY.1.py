words = input("Enter 3 words separated by space: ").split()

print("Word\t\tRoot\t\tAffix\t\tType\t\tNormalized")

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "ing"
        typ = "Inflectional"

    elif word == "analysis":
        root = "analyze"
        affix = "sis"
        typ = "Derivational"

    elif word == "analytical":
        root = "analyze"
        affix = "tical"
        typ = "Derivational"

    else:
        root = word
        affix = "-"
        typ = "Unknown"

    print(f"{word}\t{root}\t\t{affix}\t\t{typ}\t\t{root}")