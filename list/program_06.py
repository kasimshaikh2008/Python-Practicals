# Program 6: Find the maximum and minimum without using max()/min().

numbers = [45, 12, 78, 34, 9, 90, 23]
big = numbers[0]
small = numbers[0]
for n in numbers:
    if n > big:
        big = n
    if n < small:
        small = n
print("Maximum:", big)
print("Minimum:", small)
