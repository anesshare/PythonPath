import random
option = ("rock", "paper", "scissors")
player = None
computer = random.choice(option)
while player not in option:
  player = input("Enter a choice(RPS): ")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
  print("TIE!")
elif player == "rock" and computer ==" scissors":
        print("You win")
elif player == "paper" and computer ==" rock":
        print("You win")
elif player == "scissors" and computer ==" paper":
        print("You win")
else:
      print("DEFEAT")