# Program 15: Find numbers divisible by both 3 and 5

numbers = [15, 30, 45, 60, 22, 9]
result = list(filter(lambda n: n % 3 == 0 and n % 5 == 0, numbers))
print(result)
