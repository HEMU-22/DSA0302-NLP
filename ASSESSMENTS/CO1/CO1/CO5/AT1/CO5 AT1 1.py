text = """John and Mary went to the park.
He brought a ball.
She wanted to play with it.
The dog chased him excitedly.
Finally, they all went home."""

resolution = {
    "He": "John",
    "She": "Mary",
    "it": "ball",
    "him": "John",
    "they": "John + Mary + dog"
}

print("Coreference Resolution")
print("----------------------")

for reference, antecedent in resolution.items():
    print(reference, "->", antecedent)

print("\nCoreference Chains:")
print("[John] -> He -> him")
print("[Mary] -> She")
print("[Ball] -> it")
print("[John + Mary + Dog] -> they -> all")
