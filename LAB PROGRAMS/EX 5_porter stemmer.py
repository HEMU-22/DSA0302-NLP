import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = ["playing", "studies", "running", "happily", "computers", "walking"]

print("Original Word\tStemmed Word")
print("-" * 30)

for word in words:
    print(f"{word}\t\t{stemmer.stem(word)}")