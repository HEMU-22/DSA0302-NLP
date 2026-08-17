command="Book a flight to Delhi with a window seat"

print("VOICE ASSISTANT ANALYSIS")
print("Input:",command)

print("\nPossible Parse 1:")
print("BOOK(FLIGHT, DESTINATION=Delhi, SEAT=Window)")

print("\nPossible Parse 2:")
print("BOOK(FLIGHT(Delhi), WITH(WindowSeat))")

print("\nSelected Interpretation:")
print("BOOK(Flight, Destination=Delhi, Seat=Window)")

print("\nTop-Down Parsing:")
print("May require backtracking for ambiguous structures")

print("\nEarley Parsing:")
print("Maintains partial parse states and handles ambiguity efficiently")
