# Program 15: Find the average of numbers in a list.

numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
avg = total / len(numbers)
print("Average:", avg)
