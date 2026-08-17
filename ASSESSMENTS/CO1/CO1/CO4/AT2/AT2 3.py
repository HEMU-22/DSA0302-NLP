from collections import defaultdict

rules={
"S":[("VP",1.0)],
"VP":[("V NP",1.0)],
"NP":[("Det N PP",0.6),("Det N",0.4)],
"PP":[("P NP",1.0)]
}

query="Show me the transactions with the card from last month"

print("BANKING QUERY ANALYSIS")
print("Input:",query)
print("\nPossible Interpretations:")
print("1. Transactions made with the card during last month")
print("2. Transactions associated with a particular card from last month")
print("\nMost Likely Semantic Interpretation:")
print("QUERY(Transactions, Card, Time=LastMonth)")
print("\nParsing Method: Earley Parser")
print("Ambiguity Resolution: PCFG")
print("Agreement Handling: Feature Structures")
