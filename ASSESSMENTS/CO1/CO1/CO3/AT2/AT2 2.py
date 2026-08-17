import math
sentences=["Book a flight ticket now","This book is interesting"]
lexicon={"book":"NN","a":"DT","flight":"NN","ticket":"NN","now":"RB","this":"DT","is":"VBZ","interesting":"JJ"}
def rule_based(sentence):
    words=sentence.lower().split()
    result=[]
    for i,w in enumerate(words):
        if w=="book" and i==0 and len(words)>1 and words[i+1]=="a":
            tag="VB"
        elif w in lexicon:
            tag=lexicon[w]
        else:
            tag="NN"
        result.append((w,tag))
    return result
print("CASE STUDY 2")
for sentence in sentences:
    print("\nSentence:",sentence)
    for word,tag in rule_based(sentence):
        print(word,"->",tag)
p_vb=0.5*0.6
p_nn=0.5*0.4
print("\nHMM Probability")
print("P(book,VB) =",round(p_vb,4))
print("P(book,NN) =",round(p_nn,4))
if p_vb>p_nn:
    print("HMM Prediction: VB")
else:
    print("HMM Prediction: NN")
print("\nPenn Treebank Tags")
print("VB = Verb")
print("NN = Noun")
print("DT = Determiner")
print("RB = Adverb")
print("VBZ = 3rd Person Singular Verb")
print("JJ = Adjective")
