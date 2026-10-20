# Program 44: Accept a list of integers from the user. Remove all duplicate elements without using a set and display the unique list.

numbers = []
data = input("Enter numbers separated by space: ").split()
for x in data:
    numbers.append(int(x))

unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)

print("Original list:", numbers)
print("Unique list:", unique)
