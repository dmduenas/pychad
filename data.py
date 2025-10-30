import random

userpass_list = []
userpass = ""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numerics = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

def character_amount(type):
    while True:
        try:
            user_letter = int(input(f"How many {type}? "))
            return user_letter
        except ValueError:
            print("Please pick a number")

user_letters = character_amount("letters")
user_numbers = character_amount("numbers")
user_symbols = character_amount("symbols")

for x in range(user_letters):
    userpass_list.append(random.choice(alphabet))

for x in range(user_numbers):
    userpass_list.append(random.choice(numerics))

for x in range(user_symbols):
    userpass_list.append(random.choice(symbols))

random.shuffle(userpass_list)

for x in userpass_list:
    userpass = userpass + x

print(userpass)