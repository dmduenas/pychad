def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiple(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiple,
    "/": divide
    }

num1 = float(input("Enter the first number: "))

operation = input("Select an operation: ")

num2 = float(input("Enter the second number: "))


calculation_function = operation_dict[operation]


answer = calculation_function(num1, num2)
print(f"{num1} {operation} {num2} = {answer}")