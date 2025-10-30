
while True:
    new_line = input("Enter text: ")
    with open("./list.txt", mode="a") as file:
        file.write(f"{new_line}\n")
    choice = input("Would you like to enter a new entry? y/n ").lower()
    if choice == "n":
        break

