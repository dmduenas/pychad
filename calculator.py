def main():
    x = int(input("what is x? "))
    print(f"x squared is {squared(x)}")

def squared(num1):
    return num1 * num1

if __name__ == "__main__":
    main()