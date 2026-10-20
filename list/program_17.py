# Program 17: Split a list into chunks of size n.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 3
for i in range(0, len(numbers), n):
    print(numbers[i:i + n])
