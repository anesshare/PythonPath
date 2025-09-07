import random
def SpinRow():
    spins = "🍋","🍒","🍉","⭐","🔔"
    result = []
    for _ in range(3):
        result.append(random.choice(spins))
    return result
def printRow(row):
    print(" |".join(row))
def getPayout(row,bet):
    if row[0]== row[1] == row[2]:
        if row[0] =="🍋":
            return bet*3
        elif row[0] == "🍒":
            return bet*4
        elif row[0] == "🍉":
            return bet*5
        elif row[0] == "⭐":
            return bet*10
        elif row[0]== "🔔":
            return bet*20
    return 0
def main():
    balance = 100
    
    print("-------WELCOME TO CASINO--------")
    print("Symbols:🍋  🍒  🍉  ⭐  🔔 ")
    while balance>0:
        print(f"Your current balance is {balance}$")
        bet = input("Place your bet amount:")
        if not bet.isdigit():
            print("Pls enter valid number")
            continue
        bet = int(bet)
        if bet>balance:
            print("Insufficient balance")
            continue
        if bet<= 0:
            print("bet must be positive")
        balance -=bet
        row = SpinRow()
        print("Spinning...")
        print()
        printRow(row)
        payout = getPayout(row,bet)
        
        if payout >0:
            print(f"You won ${payout}")
        else:
            print("Sorry youre a loser!")
        balance +=payout
if __name__ == "__main__":
    main()