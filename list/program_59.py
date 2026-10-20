# Program 59: Accept a list of numbers and separate them into positive, negative and zero lists.

numbers = []
data = input("Enter numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))

positive = []
negative = []
zero = []
for n in numbers:
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)
    else:
        zero.append(n)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)
