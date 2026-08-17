from collections import Counter
import math
words=["economic","growth","increases","employment"]
tags=["JJ","NN","NNS","NN"]
print("CASE STUDY 3")
print("\nInitial POS Tags")
for w,t in zip(words,tags):
    print(w,"->",t)
for i in range(1,len(tags)):
    if tags[i]=="NNS" and tags[i-1]=="NN":
        tags[i]="VBZ"
print("\nCorrected POS Tags")
for w,t in zip(words,tags):
    print(w,"->",t)
frequency={"economic":120,"growth":450,"increases":210,"employment":380}
total=sum(frequency.values())
print("\nFrequency Distribution")
for word,count in frequency.items():
    probability=count/total
    print(word,":",count,"Probability =",round(probability,4))
p_before=[0.5,0.5]
p_after=[0.9,0.1]
h_before=-sum(p*math.log2(p) for p in p_before)
h_after=-sum(p*math.log2(p) for p in p_after)
print("\nEntropy Before Correction =",round(h_before,4),"bits")
print("Entropy After Correction =",round(h_after,4),"bits")
print("\nTotal Frequency =",total)
print("Entropy Reduction =",round(h_before-h_after,4),"bits")
