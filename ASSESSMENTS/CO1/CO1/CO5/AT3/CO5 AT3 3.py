dialogue = [
    ("User", "Can you book a train ticket for me?"),
    ("Agent", "Sure, where would you like to travel?"),
    ("User", "I want to go to Chennai."),
    ("Agent", "Your ticket has been booked.")
]

def identify_act(text, speaker):
    text = text.lower()

    if speaker == "User" and "can you" in text:
        return "Request"
    elif "where" in text:
        return "Question"
    elif speaker == "User" and "i want" in text:
        return "Inform"
    elif "booked" in text:
        return "Confirmation / Action"

for speaker, utterance in dialogue:
    print(speaker, ":", identify_act(utterance, speaker))

print("\nDialogue-Act Sequence:")
print("Request -> Question -> Inform -> Confirmation/Action")
