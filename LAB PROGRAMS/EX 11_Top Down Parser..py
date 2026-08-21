grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"]],
    "V": [["chased"], ["saw"]]
}

def parse(symbols, words):
    if not symbols:
        return [] if not words else None

    symbol = symbols[0]

    if symbol not in grammar:
        if words and symbol == words[0]:
            result = parse(symbols[1:], words[1:])
            if result is not None:
                return [(symbol, words[0])] + result
        return None

    for production in grammar[symbol]:
        result = parse(production + symbols[1:], words)
        if result is not None:
            return [(symbol, production)] + result

    return None

sentence = input("Enter a sentence: ").lower().split()
result = parse(["S"], sentence)

if result:
    print("Sentence Accepted")
    print("Parse:", result)
else:
    print("Sentence Rejected")