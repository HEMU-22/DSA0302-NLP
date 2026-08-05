words = input("Enter 3 words separated by space: ").split()

print("Word\t\tPrefix\tRoot\tSuffix\tType")

for word in words:

    if word == "disagree":
        prefix = "dis"
        root = "agree"
        suffix = "-"
        typ = "Derivational"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "ment"
        typ = "Derivational"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "able"
        typ = "Derivational"

    else:
        prefix = "-"
        root = word
        suffix = "-"
        typ = "Unknown"

    print(f"{word}\t{prefix}\t{root}\t{suffix}\t{typ}")