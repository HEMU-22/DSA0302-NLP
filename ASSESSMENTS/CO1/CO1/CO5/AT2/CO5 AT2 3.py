dialogue = [
    ("User", "Can you book a train ticket for me?"),
    ("Agent", "Sure, where would you like to travel?"),
    ("User", "I want to go to Chennai."),
    ("Agent", "Your ticket has been booked.")
]

def identify_act(text, speaker):
    text_lower = text.lower()

    if "can you" in text_lower or "book" in text_lower and speaker == "User":
        return "Request"
    elif "where" in text_lower:
        return "Question"
    elif "i want" in text_lower:
        return "Inform"
    elif "has been booked" in text_lower:
        return "Confirmation / Action"
    return "Unknown"

print("Dialogue Acts:")

for speaker, utterance in dialogue:
    act = identify_act(utterance, speaker)
    print(f"{speaker}: {act}")

print("\nDialogue-Act Sequence:")
print("Request -> Question -> Inform -> Confirmation/Action")
