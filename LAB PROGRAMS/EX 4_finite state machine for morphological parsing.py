# Finite State Machine for generating plural forms of English nouns

def pluralize(noun):
    # Nouns ending with s, x, z, ch, sh
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    # Nouns ending with consonant + y
    elif noun.endswith("y") and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"

    # Default rule
    else:
        return noun + "s"

# Input from user
word = input("Enter a singular noun: ")

# Display plural form
print("Plural Form:", pluralize(word))