import json

with open("question.json", 'r') as file:
    file = file.read()
    
data = json.loads(file)

score = 0
for question in data:
    print(question["Question text"])
    for i, choices in enumerate(question):
        print(i+1, "-" ,choices)
    user_choice = int(input("answer?"))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct answer"]:
        score = score + 1

print(score, "/", len(data))


for question in data:
    message = f"for the question {question['Question text']},the correct answer is {question['correct answer']}"
    print(message)    