import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.6] | 'John' [0.4]
VP -> V NP [0.7] | V [0.3]
Det -> 'the' [0.5] | 'a' [0.5]
N -> 'dog' [0.5] | 'cat' [0.5]
V -> 'sees' [0.5] | 'runs' [0.5]
""")

parser = ViterbiParser(grammar)

sentence = input("Enter a sentence: ").lower().split()

try:
    tree = next(parser.parse(sentence))
    print(tree)
    print("Probability:", tree.prob())
except StopIteration:
    print("No valid parse found")