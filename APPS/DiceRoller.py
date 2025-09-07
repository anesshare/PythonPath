import random
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 ")
"┌───────┐"
"│       │"
"│       │"
"│       │"
"└───────┘"
diceArt = {
    1:("┌───────┐",
       "│       │",
       "│   ●   │",
       "│       │",
       "└───────┘"),
    2:("┌───────┐",
       "│●      │",
       "│       │",
       "│      ●│",
       "└───────┘"),
    3:("┌───────┐",
       "│●      │",
       "│   ●   │",
       "│      ●│",
       "└───────┘"),
    4:("┌───────┐",
       "│●     ●│",
       "│       │",
       "│●     ●│",
       "└───────┘"),
    5:("┌───────┐",
       "│●     ●│",
       "│   ●   │",
       "│●     ●│",
       "└───────┘"),
    6:("┌───────┐",
       "│●     ●│",
       "│●     ●│",
       "│●     ●│",
       "└───────┘"),
}
dice=[]
total =0
numberOfDice = int(input("How many dice do you want to roll? "))
for die in range(numberOfDice):
    dice.append(random.randint(1,6))

for line in range(5):
    for die in dice:
        print(diceArt.get(die)[line],end=" ")
print()
for die in dice:
    total+=die
print(f"Total: {total}")