# Program 57: Find the second largest and second smallest element in a list without using built-in sorting.

numbers = [12, 35, 1, 10, 34, 5, 35]

largest = numbers[0]
smallest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

second_largest = None
second_smallest = None
for n in numbers:
    if n != largest:
        if second_largest == None or n > second_largest:
            second_largest = n
    if n != smallest:
        if second_smallest == None or n < second_smallest:
            second_smallest = n

print("List:", numbers)
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)
