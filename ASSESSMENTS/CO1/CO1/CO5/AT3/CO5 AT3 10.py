user_input = "Can you book a train to Chennai tomorrow?"

intent = "Request"

entities = {
    "Transport": "train",
    "Destination": "Chennai",
    "Date": "tomorrow"
}

status = "Booking request received"

response = "Your train ticket to Chennai has been booked for tomorrow."

translated_response = (
    "நாளைக்கு சென்னைக்கு உங்கள் ரயில் டிக்கெட் "
    "பதிவு செய்யப்பட்டுள்ளது."
)

print("User Input:")
print(user_input)

print("\nIntent:")
print(intent)

print("\nEntities:")
for key, value in entities.items():
    print(key, ":", value)

print("\nDialogue Status:")
print(status)

print("\nGenerated Response:")
print(response)

print("\nTranslated Response:")
print(translated_response)
