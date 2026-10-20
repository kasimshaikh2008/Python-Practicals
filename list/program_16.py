# Program 16: Find the second largest/smallest number in a list.

numbers = [12, 35, 1, 10, 34, 1, 35]
unique = []
for n in numbers:
    if n not in unique:
        unique.append(n)
unique.sort()
print("Second largest:", unique[-2])
print("Second smallest:", unique[1])
