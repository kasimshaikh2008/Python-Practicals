# Program 23: Find all pairs in a list that sum to a target value.

numbers = [1, 2, 3, 4, 5, 6, 7]
target = 8
print("Pairs with sum", target, ":")
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], "+", numbers[j], "=", target)
