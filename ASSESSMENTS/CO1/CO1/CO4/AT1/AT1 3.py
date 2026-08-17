queries={
"Apple accessories":"Technology Brand",
"Mouse wireless":"Computer Device",
"Java tutorial":"Programming Language",
"Python course":"Programming Language"
}
clicked={
"Apple accessories":"iPhone Charger",
"Mouse wireless":"Bluetooth Mouse",
"Java tutorial":"Coding Lessons",
"Python course":"Software Development Training"
}
for query,sense in queries.items():
    print("Query:",query)
    print("Clicked Result:",clicked[query])
    print("Selected Sense:",sense)
    print()
