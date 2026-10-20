# Function Program 20

nums = [12, 7, 34, 21, 8, 15, 40, 9]
even = list(filter(lambda x: x % 2 == 0, nums))
odd = list(filter(lambda x: x % 2 != 0, nums))
print("Even numbers:", even)
print("Odd numbers:", odd)
