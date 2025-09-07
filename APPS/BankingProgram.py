def showBalance():
    print(f"Your current balance is ${balance:.2f}.")
def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0:
        print("Not a valid amount!")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter an amount u want to withdraw: "))
    if amount<0:
        print("Not a valid amount!")
        return 0
    elif amount>balance:
        print("Insufficient funds")
        return 0

    else:
        return amount

balance = 0
isRunning = True

while isRunning:
    print("--WELCOME TO THE GNB--")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Quit")
    choice=input("Please enter your choice: ")
    if choice == "1":
        showBalance()
    elif choice == "2":
        balance +=deposit()
    elif choice == "3":
        balance -=withdraw()
    elif choice == "4":
        isRunning = False
    else:
        print("Invalid choice!")
print("Have a nice day!")