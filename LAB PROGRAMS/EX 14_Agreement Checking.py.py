grammar = {
    "singular_subjects": ["he", "she"],
    "plural_subjects": ["they", "we"],
    "singular_verbs": ["runs", "plays", "eats"],
    "plural_verbs": ["run", "play", "eat"]
}

def check_agreement(sentence):
    words = sentence.lower().split()

    if len(words) != 2:
        return False

    subject = words[0]
    verb = words[1]

    if subject in grammar["singular_subjects"] and verb in grammar["singular_verbs"]:
        return True

    if subject in grammar["plural_subjects"] and verb in grammar["plural_verbs"]:
        return True

    return False

sentence = input("Enter a sentence: ")

if check_agreement(sentence):
    print("Agreement is Correct")
else:
    print("Agreement is Incorrect")