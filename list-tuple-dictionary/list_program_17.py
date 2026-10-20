# List Program 17
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
odd = [x for x in nums if x % 2 != 0]
even = [x for x in nums if x % 2 == 0]
print("Odd list:", odd)
print("Even list:", even)
