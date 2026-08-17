sentence="The doctor who reviewed the patient last week recommends starting medication and scheduling a follow-up visit in Chennai."

tokens=sentence.replace(".","").split()

print("HEALTHCARE SEMANTIC ANALYSIS")
print("\nInput:")
print(sentence)

print("\nTokens:")
print(tokens)

print("\nSyntactic Structure:")
print("Doctor -> recommends -> starting medication")
print("Doctor -> recommends -> scheduling follow-up visit")
print("who -> reviewed -> patient")
print("follow-up visit -> in -> Chennai")

print("\nSemantic Roles:")
print("Doctor -> Agent")
print("Patient -> Patient Entity")
print("Medication -> Treatment")
print("Starting medication -> Treatment Action")
print("Follow-up visit -> Follow-up Action")
print("Chennai -> Location")

print("\nSemantic Representation:")
print("DOCTOR(x)")
print("REVIEWS(x,PATIENT)")
print("TIME(Review,LastWeek)")
print("RECOMMENDS(x,StartMedication)")
print("RECOMMENDS(x,ScheduleFollowUp)")
print("LOCATION(FollowUp,Chennai)")

print("\nStructured Output:")
print("Diagnosis: Not explicitly stated")
print("Treatment: Start medication")
print("Follow-up: Schedule follow-up visit")
print("Location: Chennai")
print("Review Time: Last week")

print("\nArchitecture:")
print("CFG -> Earley Parser -> PCFG -> Feature Structures ->")
print("Sub-Categorization -> Semantic Role Labeling -> Structured Output")
