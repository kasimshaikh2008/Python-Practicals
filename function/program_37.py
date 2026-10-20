# Function Program 37

from functools import reduce
nums = [2, 3, 4, 5]
result = reduce(lambda a, b: a * b, nums)
print("Product:", result)
