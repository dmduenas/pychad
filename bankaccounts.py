import random


while True:

    user_choice = input("Roll the dice? y / n: ").lower()

    if user_choice == "y":

        dice_roll_a = random.randrange(1, 10)
        dice_role_b = random.randrange(1, 10)

        print(f"{dice_roll_a}, {dice_role_b}")

    elif user_choice == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid Choice")