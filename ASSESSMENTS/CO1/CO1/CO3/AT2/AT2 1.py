from collections import Counter
import math
corpus="data science is powerful data science drives innovation data science is evolving".lower().split()
uni=Counter(corpus)
bi=Counter(zip(corpus[:-1],corpus[1:]))
tri=Counter(zip(corpus[:-2],corpus[1:-1],corpus[2:]))
def unigram(w):
    return uni[w]/len(corpus) if uni[w]>0 else 0
def bigram(w1,w2):
    return bi[(w1,w2)]/uni[w1] if uni[w1]>0 else 0
def trigram(w1,w2,w3):
    return tri[(w1,w2,w3)]/bi[(w1,w2)] if bi[(w1,w2)]>0 else 0
print("CASE STUDY 1")
p1=bigram("data","science")
print("P(science|data) =",round(p1,4))
p3=trigram("data","science","improves")
p2=bigram("science","improves")
p0=unigram("improves")
if p3>0:
    backoff=p3
elif p2>0:
    backoff=p2
else:
    backoff=p0
print("Backoff P(improves|data science) =",round(backoff,4))
pt=trigram("data","science","is")
pb=bigram("science","is")
pu=unigram("is")
di=0.5*pt+0.3*pb+0.2*pu
print("Trigram Probability =",round(pt,4))
print("Bigram Probability =",round(pb,4))
print("Unigram Probability =",round(pu,4))
print("Deleted Interpolation =",round(di,4))
p=[0.66,0.33]
entropy=-sum(x*math.log2(x) for x in p if x>0)
print("Entropy =",round(entropy,4),"bits")
