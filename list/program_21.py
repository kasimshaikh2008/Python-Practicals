# Program 21: Rotate a list left/right by n positions.

numbers = [1, 2, 3, 4, 5, 6]
n = 2
n = n % len(numbers)
left = numbers[n:] + numbers[:n]
right = numbers[-n:] + numbers[:-n]
print("Original:", numbers)
print("Rotated left by", n, ":", left)
print("Rotated right by", n, ":", right)
