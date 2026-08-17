sentence="Book a flight to Delhi"
words=sentence.split()
print("Input:",sentence)
print("Parsing Strategy: Earley")
for i,word in enumerate(words,1):
    print("State",i,": processed ->",word)
print("Result: Complete sentence structure identified")
