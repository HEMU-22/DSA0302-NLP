queries=[
("Activate international roaming","ACTIVATE","Roaming"),
("Deactivate caller tune service","DEACTIVATE","CallerTune"),
("Check my data balance","QUERY","DataBalance"),
("Enable 5G service","ACTIVATE","5GService")
]
logs=[
("Activate Roaming","Activate Roaming"),
("Deactivate Caller Tune","Activate Caller Tune"),
("Check Data Balance","Query Data Balance"),
("Enable 5G Service","Activate 5G Service")
]
print("SEMANTIC REPRESENTATION")
for q,a,o in queries:
    print(q,"->",a+"("+o+", Customer)")
correct=0
for actual,predicted in logs:
    if actual.lower()==predicted.lower():
        correct+=1
    print("Actual:",actual,"Predicted:",predicted)
accuracy=correct/len(logs)*100
print("Correct Predictions:",correct)
print("Accuracy:",accuracy,"%")
print("Error: Q2 action should be DEACTIVATE, not ACTIVATE")
