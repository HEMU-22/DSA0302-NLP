import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'mouse'
V -> 'chased' | 'saw'
""")

parser = ChartParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No parse tree found")