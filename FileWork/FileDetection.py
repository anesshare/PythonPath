import os       #Omogucava biblioteka da se komunicira sa podacima iz os


file_path = "text.txt"
if os.path.exists(file_path):       #Ugradna funkcija od import os za proveru vraca boolean
    print(f"File good {file_path}")
    if os.path.isfile(file_path):
        print("It is a file!")
else:
    print("There is no location of this")