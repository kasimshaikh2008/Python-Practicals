# Program 32: Find the longest consecutive sequence of numbers.

numbers = [100, 4, 200, 1, 3, 2, 101, 5]
numbers.sort()
longest = 1
current = 1
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1] + 1:
        current += 1
    elif numbers[i] != numbers[i - 1]:
        current = 1
    if current > longest:
        longest = current
print("Sorted list:", numbers)
print("Longest consecutive sequence length:", longest)
