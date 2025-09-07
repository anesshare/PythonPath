#Oni proveravaju da li vrednost ili variabla je ukljucena u npr string,listu,itd
word ="Apple"
letter = input("Guess a letter")
if letter in word:               #in vraca true ili false
    print(f"There is an {letter}")
else:
    print(f"{letter} not found ")