import random
import string
length = int(input("Enter the length of the password: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(characters, k=length))
print("Your password is:", password)