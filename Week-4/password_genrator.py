import random
import string
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
characters = letters + digits + symbols

def password_genrator():
    length = int(input("Enter Password Length: "))
    if length <= 0:
        print("Enter a positive length")
    password =""
    for i in range(length):
        password += random.choice(characters)
    print(f"Generated Password: {password}") 

password_genrator()
