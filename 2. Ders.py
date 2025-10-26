import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pass_length = int(input("Lütfen şifrenizin uzunluğunu seçiniz"))

password = ""
for char in range(pass_length):
    password += random.choice(chars)
print(password)
