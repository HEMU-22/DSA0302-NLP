words = input("Enter 3 words separated by space: ").split()

print("Word\t\tRoot\t\tSuffix\t\tType\t\tNormalized")

for word in words:

    if word == "govern":
        root = "govern"
        suffix = "-"
        typ = "Base"

    elif word == "government":
        root = "govern"
        suffix = "ment"
        typ = "Derivational"

    elif word == "governance":
        root = "govern"
        suffix = "ance"
        typ = "Derivational"

    else:
        root = word
        suffix = "-"
        typ = "Unknown"

    print(f"{word}\t{root}\t\t{suffix}\t\t{typ}\t\t{root}")