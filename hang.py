import random

hidden_number = random.randint(1, 101)

difficulty = input("Pick a difficulty- Easy or Hard? ").lower()

if difficulty == "easy":
    life = 10
else:
    life = 5

while life > 0:
    user_choice = int(input("Pick a number between 1 and 100: "))
    if user_choice == hidden_number:
        print("You guessed it right!")
        break
    elif hidden_number > user_choice:
        life -= 1
        if life > 0:
            print(f"Too low. Guess again. {life} life remaining")
        else:
            print("Game Over")
    else:
        life -= 1
        if life > 0:
            print(f"Too high. Guess again {life} life remaining")
        else:
            print("Game Over")