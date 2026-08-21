import re

def parse_fopc(expression):
    expression = expression.strip()

    pattern = r'^(forall|exists)\s+([a-zA-Z]+)\s*\((.*)\)$'
    match = re.match(pattern, expression)

    if match:
        return {
            "Quantifier": match.group(1),
            "Variable": match.group(2),
            "Predicate": match.group(3)
        }

    pattern = r'^([A-Za-z]+)\((.*?)\)$'
    match = re.match(pattern, expression)

    if match:
        return {
            "Predicate": match.group(1),
            "Arguments": match.group(2).split(",")
        }

    return None

expression = input("Enter FOPC expression: ")

result = parse_fopc(expression)

if result:
    print("\nParsed Expression:")
    for key, value in result.items():
        print(key, ":", value)
else:
    print("Invalid FOPC expression")
    print()