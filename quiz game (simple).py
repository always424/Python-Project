# quiz game (simple)

questions = ("How many elements in the periodic table?: ",
            "Which animal lays the largest eggs? : ",
            "Which is the most abundant gas is Earth's atmosphere? : ",
            "How many bones are there in the human body? : ")
options = (("A. 116" , "B. 117", "C. 118","D. 119"),
          ("A. Whale" , "B. Crocodile", "C. Elephant","D. Ostrich"),
          ("A. Nitrogen" , "B. Oxygen", "C. Carbon-Dioxide","D. Hydrogen"),
          ("A. 206" , "B. 207", "C. 208","D. 209"))

answers = ("C","D","A","A")
guesses = []
score = 0
questions_num = 0

for question in questions:
    print("------------------------------------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    guess = input("Enter A B C D : ").upper()
    guesses.append(guess)
    if guess == answers[questions_num]:
        print("Correct!!")
        score+=1
    else:
        print("Incorrect")
        print(f"{answers[questions_num]} is the correct answer")

    questions_num+=1


print("------------------------------------------------------")
print("------------------------------------------------------")
print("                  THE RESULT                          ")
print("------------------------------------------------------")
print("------------------------------------------------------")

print("Answer : ", end=" ")
for answer in answers:
    print(answer,end=" ")
print("Guesses",end=" ")
for guess in guesses:
    print(guess , end=" ")
print()
score = score / len(questions) * 100
print(f"Your score is {score}%")
