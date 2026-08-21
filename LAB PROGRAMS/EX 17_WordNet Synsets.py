import nltk
from nltk.corpus import wordnet

nltk.download("wordnet")
nltk.download("omw-1.4")

word = input("Enter a word: ")

synsets = wordnet.synsets(word)

print("\nSynsets:")

for syn in synsets:
    print("Synset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
    print()