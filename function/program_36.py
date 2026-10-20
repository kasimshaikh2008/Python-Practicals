# Function Program 36

from functools import reduce
nums = [10, 20, 30, 40]
total = reduce(lambda a, b: a + b, nums)
print("Sum:", total)
