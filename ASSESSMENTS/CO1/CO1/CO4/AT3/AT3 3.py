parses={"She uses telescope":0.70,"Man has telescope":0.30}
best=max(parses,key=parses.get)
print("Sentence: She saw the man with a telescope.")
print("Possible interpretations:")
for k,v in parses.items():
    print(k,"->",v)
print("Selected interpretation:",best)
