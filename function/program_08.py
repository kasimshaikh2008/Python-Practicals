# Function Program 8

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Prime numbers between", start, "and", end)
for i in range(start, end + 1):
    if is_prime(i):
        print(i)
