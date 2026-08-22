source = "The boy is playing football."

source_structure = {
    "Subject": "boy",
    "Verb": "playing",
    "Object": "football",
    "Tense": "present continuous"
}

target_structure = {
    "Subject": "சிறுவன்",
    "Object": "கால்பந்து",
    "Verb": "விளையாடுகிறான்"
}

translation = "சிறுவன் கால்பந்து விளையாடுகிறான்."

print("Source:", source)

print("\nSource Analysis:")
for key, value in source_structure.items():
    print(key, ":", value)

print("\nTarget Structure:")
for key, value in target_structure.items():
    print(key, ":", value)

print("\nTranslation:")
print(translation)
