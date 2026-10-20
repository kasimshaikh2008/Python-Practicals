# Program 52: Accept a list of numbers and perform slicing operations.

numbers = []
data = input("Enter at least 10 numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))

print("First five elements:", numbers[:5])
print("Last five elements:", numbers[-5:])
print("Alternate elements:", numbers[::2])
print("Reversed list:", numbers[::-1])
