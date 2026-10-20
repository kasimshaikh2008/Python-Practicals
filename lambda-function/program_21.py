# Program 21: Find the second-largest distinct number

numbers = [10, 5, 8, 20, 20, 15]
unique_numbers = list(set(numbers))
largest = max(unique_numbers)
second_largest = max(filter(lambda n: n < largest, unique_numbers))
print(second_largest)
