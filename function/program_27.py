# Function Program 27

nums = [1, 2, 3, 3, 4, 5, 5, 6]
result = list(filter(lambda x: nums.count(x) == 1, nums))
print(result)
