# Program 22: Remove all occurrences of a specific value.

numbers = [1, 2, 3, 2, 4, 2, 5]
value = 2
result = []
for n in numbers:
    if n != value:
        result.append(n)
print("Original:", numbers)
print("After removing", value, ":", result)
