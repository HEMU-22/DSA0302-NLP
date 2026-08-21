responses = [
    "Since your exam is tomorrow, take a short break and return with a clear focus. Stay confident by studying one small topic at a time.",

    "Because the exam is important, take a short break if you cannot concentrate, then focus on one topic at a time. Stay confident and follow a calm study plan.",

    "Your exam is tomorrow, so take a short break to refresh your mind and improve your focus. Stay confident and concentrate on the most important topics first."
]

keywords = ["focus", "break", "confident"]

for i, response in enumerate(responses, 1):
    sentences = response.count(".")
    found_keywords = [k for k in keywords if k in response.lower()]

    print("Response", i)
    print(response)
    print("Sentences:", sentences)
    print("Keywords:", found_keywords)
    print()
