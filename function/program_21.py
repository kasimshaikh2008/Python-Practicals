# Function Program 21

f = lambda a, b: a * b if type(a) == int and type(b) == int else str(a) + str(b)
a = input("Enter first value: ")
b = input("Enter second value: ")
if a.isdigit():
    a = int(a)
if b.isdigit():
    b = int(b)
print("Result:", f(a, b))
