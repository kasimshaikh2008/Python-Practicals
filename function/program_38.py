# Function Program 38

from functools import reduce
nums = [45, 12, 78, 34, 90, 23]
result = reduce(lambda a, b: a if a > b else b, nums)
print("Maximum:", result)
