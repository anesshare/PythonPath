import random
import string
chars =" "+ string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)
#ENCRYPT
plainText = input("Enter a message to encrypt: ")
encryptedMessage = ""
for letter in plainText:
    index = chars.index(letter)
    encryptedMessage += key[index]
print(f"original: {plainText} and encrypted: {encryptedMessage}")

#DECRYPT
encryptedMessage = input("Enter a message to decrypt ")
plainText = ""
for letter in encryptedMessage:
    index = key.index(letter)
    plainText += chars[index]
print(f"original: {encryptedMessage} and encrypted: {plainText}")
