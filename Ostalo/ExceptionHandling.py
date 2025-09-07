#Postoje exception sledece ZeroDivisonError,TypeError,ValueError
#Resavamo ih klasika try catch finally
try:
    num = int(input("enter a num"))
    print(1/num)
except ZeroDivisionError:
    print("Ne mozete da delite sa 0")
except ValueError:
    print("Samo brojevi")
except Exception:
    print("Nesto se desilo :/")
finally:
    print("Nesto se desilo")