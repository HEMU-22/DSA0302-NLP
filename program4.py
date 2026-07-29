def pluralize(noun):

    if noun.endswith("y") and noun[-2].lower() not in "aeiou":
        return noun[:-1] + "ies"

    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"

    else:
        return noun + "s"


noun = input("Enter a noun: ")

print("Singular:", noun)
print("Plural:", pluralize(noun))