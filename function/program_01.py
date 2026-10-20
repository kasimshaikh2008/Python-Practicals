# Function Program 1

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def int_div(a, b):
    return a // b
def power(a, b):
    return a ** b
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Integer Division")
    print("6. Power")
    print("7. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 7:
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if ch == 1:
        print("Result:", add(a, b))
    elif ch == 2:
        print("Result:", sub(a, b))
    elif ch == 3:
        print("Result:", mul(a, b))
    elif ch == 4:
        print("Result:", div(a, b))
    elif ch == 5:
        print("Result:", int_div(a, b))
    elif ch == 6:
        print("Result:", power(a, b))
    else:
        print("Invalid choice")
