import random
# low =1
# high = 100
# opt = ("rock", "paper", "scissors")
# opt1=random.choice(opt)
# print(opt1)
# cards=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# random.shuffle(cards)
# print(cards)

#NumberGuessingGame
low = 1
high = 100
number = random.randint(low, high)
guesses = 0
isRunning = True
print("Welcome to Number Guessing GAME!!!!")
print(f"Select a number between {low} and {high}")
while isRunning:
    guess = input("Enter your guess: ")
    if guess.isdigit:
        guess = int(guess)
        guesses+=1
        if guess< low or guess>high:
            print("Invalid number")
            print(f"Select a number between {low} and {high}")
        elif guess<number:
            print("Number is too low!")
        elif guess>number:
            print("Number is too high!")
    
        else:
            print(f"Correct!!! The answer was {number}")
            print(f"Number of guesses: {guesses}")
            isRunning = False

        
    else:
        print("Invalid guess")
        print(f"Select a number between {low} and {high}")
