questions = {
    "What is 15*3?":{"correct":"a", "answers":[45,35,60,40,30]},
    "What is 17 * 2?":{"correct":"b", "answers":[43,34,36,32,30]},
    "What is 19 * 3?":{"correct":"e", "answers":[58,48,55,59,57]},
    "What is 22 * 7?":{"correct":"c", "answers":[168,152,154,156,161]}
}
anslabels = ['a','b','c','d','e']
correct = 0
total = len(questions)
input("\nThank you for trying out William Passmore's Python 3 Quiz!\nPress ENTER to start!\n")
for k, v in questions.items():
    print(k)
    x = 0
    for ans in v["answers"]:
        print(anslabels[x] + ": " + str(ans))
        x += 1
    answer = input("\nType a, b, c, d, or e to select your answer. Then press ENTER.\n")
    if(answer == v["correct"]):
        correct += 1
    print("\n")
score = str((correct / total) * 100) + "%"
print("Quiz Complete!\nYour score is " + score + " on this quiz.")
