sentences=[
("Doctor prescribed medicine to patient",{"Doctor":"Agent","medicine":"Theme","patient":"Recipient"}),
("Patient reported severe headache",{"Patient":"Experiencer","headache":"Symptom"}),
("Nurse monitored patient continuously",{"Nurse":"Agent","patient":"Patient"}),
("Medicine reduced blood pressure",{"Medicine":"Agent","blood pressure":"Affected Condition"})
]
for sentence,roles in sentences:
    print("\nSentence:",sentence)
    for entity,role in roles.items():
        print(entity,"->",role)
