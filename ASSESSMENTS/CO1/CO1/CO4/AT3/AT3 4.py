subject={"word":"student","number":"singular"}
verb={"word":"reads","number":"singular"}
if subject["number"]==verb["number"]:
    print("Agreement: Correct")
else:
    print("Agreement: Error")
frames={"eat":"NP","give":"NP NP","depend":"PP"}
print("prescribe -> NP")
print("give -> NP NP")
