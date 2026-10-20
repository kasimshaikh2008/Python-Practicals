# Program 34: Find cubes of numbers divisible by 3

numbers = [1, 2, 3, 4, 6, 8, 9]
selected = filter(lambda n: n % 3 == 0, numbers)
result = list(map(lambda n: n ** 3, selected))
print(result)
