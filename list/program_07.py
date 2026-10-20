# Program 7: Count how many times a value appears in a list.

numbers = [1, 2, 3, 2, 4, 2, 5]
value = 2
count = 0
for n in numbers:
    if n == value:
        count += 1
print(value, "appears", count, "times")
