# Program 58: Create a list of numbers and replace every negative number with zero.

numbers = [5, -3, 8, -1, 0, -7, 12]
print("Original:", numbers)
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print("After replacing negatives:", numbers)
