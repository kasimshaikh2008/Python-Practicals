# Program 12: Find odd numbers in a list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(filter(lambda n: n % 2 != 0, numbers))
print(result)
