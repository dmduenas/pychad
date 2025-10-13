def addition(x, y):
    """Adds the two numbers"""
    answer = x + y
    return answer

def subtraction(x, y):
    """Subtracts the two numbers"""
    answer = x - y
    return answer

def multiplication(x, y):
    """Multiplies the two numbers"""
    answer = x * y
    return answer

def division(x, y):
    """Divides the two numbers"""
    answer = x / y
    return answer


status = True
num1 = float(input("\nWhat is the first number? "))

while status:
    operation = input("\nPlease select an operation\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n")
    num2 = float(input("What is the second number? "))

    if operation == "1":
        data = addition(num1, num2)
        print(f"\nAnd the answer is {data}")


    elif operation == "2":
        print(f"\nAnd the answer is {subtraction(num1, num2)}")

    elif operation == "3":
        print(f"\nAnd the answer is {multiplication(num1, num2)}")

    elif operation == "4" and num2 == 0:
        print(f"\nYou may can't divide a number by Zero")

    elif operation == "4":
        print(f"\nAnd the answer is {division(num1, num2)}")

    else:
        print("\nPlease select a valid operation")


    user_choice = input("Do you want to run the program again? [Yes / No] ").lower()

    if user_choice == "no":
        status = False
 

    