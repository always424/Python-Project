questions = []
options = []
answers = []
num_questions = int(input("Enter the number of questions: "))

for i in range(num_questions):
    question = input(f"Enter question {i+1}: ")
    questions.append(question)
    
    option_list = []
    for j in range(4):
        option = input(f"Enter option {chr(65+j)}: ")
        option_list.append(f"{chr(65+j)}. {option}")
    options.append(tuple(option_list))
    
    correct_answer = input("Enter the correct option (A, B, C, or D): ").upper()
    answers.append(correct_answer)

guesses = []
score = 0

for idx, question in enumerate(questions):
    print("------------------------------------------------------")
    print(question)
    for option in options[idx]:
        print(option)
    
    guess = input("Enter A, B, C, or D: ").upper()
    guesses.append(guess)
    
    if guess == answers[idx]:
        print("Correct!!")
        score += 1
    else:
        print("Incorrect")
        print(f"{answers[idx]} is the correct answer")

print("------------------------------------------------------")
print("                  THE RESULT                          ")
print("------------------------------------------------------")
print("Answer  :", " ".join(answers))
print("Guesses :", " ".join(guesses))
score = (score / num_questions) * 100
print(f"Your score is {score}%")
