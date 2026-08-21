grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"]],
    "V": [["chased"], ["saw"]]
}

def earley_parse(words):
    n = len(words)
    chart = [[] for _ in range(n + 1)]
    chart[0].append(("S", ["NP", "VP"], 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for lhs, rhs, dot, start in chart[i][:]:
                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for production in grammar[symbol]:
                            item = (symbol, production, 0, i)
                            if item not in chart[i]:
                                chart[i].append(item)
                                changed = True

                    elif i < n and rhs[dot] == words[i]:
                        item = (lhs, rhs, dot + 1, start)
                        if item not in chart[i + 1]:
                            chart[i + 1].append(item)

                else:
                    for plhs, prhs, pdot, pstart in chart[start]:
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            item = (plhs, prhs, pdot + 1, pstart)
                            if item not in chart[i]:
                                chart[i].append(item)
                                changed = True

    return ("S", ["NP", "VP"], 2, 0) in chart[n]

sentence = input("Enter a sentence: ").lower().split()

if earley_parse(sentence):
    print("Sentence Accepted")
else:
    print("Sentence Rejected")