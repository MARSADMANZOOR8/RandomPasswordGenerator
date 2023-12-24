import secrets
import random
import string
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
List = letters+digits+special_chars
Password_Length = int(input("Enter the password Length You want to Generate "))
Password = ''
for i in range(Password_Length):
    Password+= ''.join(secrets.choice(List))
print(Password)
