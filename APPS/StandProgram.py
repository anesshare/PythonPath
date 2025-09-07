menu ={
    "item":3.00,
    "drink": 1.50,
    "dessert": 2.50,  
    "combo": 5.00
}
cart =[]
total = 0.00
for key,value in menu.items():
    print(f"{key}: {value:.2f}")
while True:
    food = input("Select an item,Q to quit: ")
    if food == "q" or food == "Q":
        break
    elif  menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Total is {total:.2f}")

#KUPOVINA NA STAND U BIOSKOP SIMULACIJA