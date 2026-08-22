source = "The boy is playing football."

interlingua = {
    "Action": "PLAY",
    "Agent": "BOY",
    "Object": "FOOTBALL",
    "Tense": "PRESENT_CONTINUOUS"
}

translations = {
    "Tamil": "சிறுவன் கால்பந்து விளையாடுகிறான்.",
    "Hindi": "लड़का फुटबॉल खेल रहा है."
}

print("Source:")
print(source)

print("\nInterlingua:")
for key, value in interlingua.items():
    print(key, "=", value)

print("\nGenerated Translations:")
for language, translation in translations.items():
    print(language, ":", translation)
