import json
import time


file = open("file.json", "r")

questionSet = file.read()
questionList = json.loads(questionSet)

j = 0
correct = 0
incorrect = 0
time_array = []

print("Choose correct answer from a to d")


start = time.time()
for i in questionList["Math_quiz"]:
    j += 1
    print("Question " + str(j))
    s = "q" + str(j)
    print(questionList["Math_quiz"][j-1][s]["question"])
    print("<a> " + questionList["Math_quiz"][j - 1][s]["options"][0])
    print("<b> " + questionList["Math_quiz"][j - 1][s]["options"][1])
    print("<c> " + questionList["Math_quiz"][j - 1][s]["options"][2])
    print("<d> " + questionList["Math_quiz"][j - 1][s]["options"][3])
    correctAnswer = questionList["Math_quiz"][j - 1][s]["correct"]
    startQ = time.time()
    userAnswer = input()
    while userAnswer != 'a' and userAnswer != 'b' and userAnswer != 'c' and userAnswer != 'd':
        print("There is no such an answer. Try using a, b, c or d.")
        userAnswer = input()
    endQ = time.time()
    match userAnswer:
        case 'a':
            answer = questionList["Math_quiz"][j - 1][s]["options"][0]
        case 'b':
            answer = questionList["Math_quiz"][j - 1][s]["options"][1]
        case 'c':
            answer = questionList["Math_quiz"][j - 1][s]["options"][2]
        case 'd':
            answer = questionList["Math_quiz"][j - 1][s]["options"][3]
        case _:
            answer = ''
    if correctAnswer == answer:
        correct += 1
    else: incorrect += 1
    time_array.append(endQ - startQ)

end = time.time()

print()
print("Your score")
print("Correct answers: " + str(correct))
print("Incorrect answers: " + str(incorrect))
print("Time spent on survey: " + str(round(end - start, 2)))
j = 1
for i in time_array:
    print("Time spend on " + str(j) + " question: " + str(round(i, 2)))
    j += 1

file.close()