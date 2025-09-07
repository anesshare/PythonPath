# def Ispisi(name):
#     print(f"Happy birthday {name}")

# def display_invoice(user,amoun,date):
#     print(f"Hello {user}")    
#     print(f"Your bill amount: {amoun:.2f} is due {date}")
# def add(x,y):
#     z =x+y
#     return z
# def subtract(x,y):
#     z =x-y
#     return z
# def multiply(x,y):
#     z =x*y
#     return z
# def divide(x,y):
#      z = x / y
#      return z
# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide (1,2))


#default args
# import time
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done")
# count(10)

#keyword args
# def getCode(count,area,first,last):
#     return f"{count}-{area}-{first}-{last}"
# phone = getCode(count=381,area=123,first=456,last=7890)
# print(phone)

#Arbitrary args koristi se kad ne znamo koliko ce argumenata imati
def add(*args):
    total =0
    for arg in args:
         total+=arg
    return total
print(add(1,2,3))