fruits = ["apple","banana","ananas"]
vegetables = ["watermelon","tomato","potato"]
meats = ["chicken","fish","biftec"]
groceries = [fruits,vegetables,meats]
for grocery in groceries:
    for element in grocery:
        print(element,end=" ")

    print()