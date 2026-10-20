# Program 63: Accept a list of integers and find all missing numbers between the minimum and maximum value.

numbers = []
data = input("Enter numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))

small = min(numbers)
big = max(numbers)
missing = []
for i in range(small, big + 1):
    if i not in numbers:
        missing.append(i)

print("List:", numbers)
print("Missing numbers:", missing)
