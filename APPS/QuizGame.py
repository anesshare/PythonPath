questions=["Who is the best shooter: ",
           "When will anes marry: ",
           "Where is anes working: ",
           "How much is his salary: ",
           "How old is  anes: "]
options = (("A.Steph","B. Lebron","C. Durant","D. Tatum"),
           ("A. 2025","B. 2026","C.2027","D. 2028"),
           ("A.Microsof","B. Art","C. Levi9","D. Nvidia"),
           ("A. 10k","B. 150k","C. 60k","D. 80k"),
           ("A. 19","B. 22","C. 24","D. 23"))
answers = ("A","B","B","C","D")
guesses=[]
score = 0
question_num = 0
for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score+=20
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is correct answer!")
    question_num+=1   
    print(f"YOUR SCORE IS {score}")

