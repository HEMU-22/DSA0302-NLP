# Finite State Automaton to recognize strings ending with 'ab'

def fsa(string):
    if string.endswith("ab"):
        print("Accepted")
    else:
        print("Rejected")

# Input from user
text = input("Enter a string: ")

# Function call
fsa(text)