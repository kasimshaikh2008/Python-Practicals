# List Program 16
nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
odd_total = 0
even_total = 0
for n in nums:
    if n % 2 == 0:
        even_total = even_total + n
    else:
        odd_total = odd_total + n
print("Total of odd numbers:", odd_total)
print("Total of even numbers:", even_total)
