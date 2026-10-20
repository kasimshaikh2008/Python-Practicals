# Program 30: Find the sum using reduce()

from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, numbers)
print(result)
