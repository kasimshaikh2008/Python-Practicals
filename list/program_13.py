# Program 13: Remove duplicates from a list.

numbers = [1, 2, 2, 3, 4, 4, 5, 1]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
print("Original:", numbers)
print("Without duplicates:", unique)
