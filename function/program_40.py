# Function Program 40

fact = lambda n: 1 if n == 0 else n * fact(n - 1)
n = int(input("Enter a number: "))
print("Factorial:", fact(n))
