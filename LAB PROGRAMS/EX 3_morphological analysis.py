import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download tokenizer (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

# Create stemmer
stemmer = PorterStemmer()

# Input sentence
text = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(text)

print("\nMorphological Analysis (Stemming):")
for word in words:
    print(word, "->", stemmer.stem(word))