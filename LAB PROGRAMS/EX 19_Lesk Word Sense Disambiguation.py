import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")

sentence = input("Enter a sentence: ")
word = input("Enter the word to disambiguate: ")

tokens = nltk.word_tokenize(sentence)

sense = lesk(tokens, word)

if sense:
    print("\nWord:", word)
    print("Synset:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")