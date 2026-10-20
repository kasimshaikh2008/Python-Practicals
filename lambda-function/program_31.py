# Program 31: Find the maximum using reduce()

from functools import reduce
numbers = [12, 45, 7, 89, 34]
result = reduce(lambda a, b: a if a > b else b, numbers)
print(result)
